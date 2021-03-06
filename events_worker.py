#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
from datetime import date, timedelta, datetime
import traceback
import telebot
import time
import config
from models import Events, Exodus_Users, session, update_event
from events import invitation_help_orange, invitation_help_red, notice_of_intent, obligation_sended_notice, \
    obligation_recieved_notice, obligation_money_requested_notice, reminder, reminder_for_6_10, \
    check_border_before_3_days, check_border_first_date, create_future_intention

bot = telebot.TeleBot(config.API_TOKEN)

# --------------------------------- DB ------------------------------


user_dict = {}
bot.remove_webhook()

# завели списки, чтобы добавить туда event_id отправленных уведомлений
list_event_id_obligation_sended = []
list_event_id_obligation_recieved = []
list_event_id_for_6_10 = []

check_in_first_day = [1]

def read():
    # all_users = session.query(Exodus_Users).count()
    all = session.query(Events).filter_by(sent=False)
    current_date = date.today()
    day_now = datetime.now().day

    check_day = 1

    if (datetime.now() + timedelta(days=3)).day == check_day:
        check_border_before_3_days()
        check_in_first_day[0] = 1
    elif day_now == check_day and check_in_first_day[0] == 1:
        #check_in_first_day = False
        check_border_first_date()
        check_in_first_day[0] = 0


    for event in all:
        # проверяем событие из будущего, чтобы 1 числа создать intetion со статусом 1
        if event.type == 'future_event' and day_now == check_day:
            create_future_intention(event)

        if event.type == 'orange':
            # print('Отправлен orange {}'.format(event.event_id))
            update_event(event.event_id, True)
            invitation_help_orange(event.event_id)
        if event.type == 'red':
            # print('Отправлен red {}'.format(event.event_id))
            update_event(event.event_id, True)
            invitation_help_red(event.event_id)
        if event.type == 'notice' and event.status == 'orange':
            # print('Отправлен notice {}'.format(event.event_id))
            update_event(event.event_id, True)
            notice_of_intent(event.event_id)
        # 6.4
        # if event.type == 'obligation_sended' and (current_date == event.reminder_date or
        #                                           current_date > event.reminder_date) and event.event_id not in list_event_id_obligation_sended:
        #     list_event_id_obligation_sended.append(event.event_id)
        #
        #     obligation_sended_notice(event.event_id)

        # 6.9
        if event.type == 'obligation_recieved' and (current_date == event.reminder_date or
                                                    current_date > event.reminder_date):
            list_event_id_obligation_recieved.append(event.event_id)

            obligation_recieved_notice(event.event_id)
            update_event(event.event_id, True)

        if event.type == 'obligation_money_requested' and (current_date == event.reminder_date or
                                                           current_date > event.reminder_date):
            update_event(event.event_id, True)
            obligation_money_requested_notice(event.event_id)

        if event.type == 'reminder_out' and \
                (current_date == event.reminder_date or current_date > event.reminder_date):
            update_event(event.event_id, True)
            # update_event_status_code(event.event_id, status_code=CLOSED)
            reminder(event.event_id, direction='out')  # 6.3, 6.7

        if event.type == 'reminder_in' and \
                (current_date == event.reminder_date or current_date > event.reminder_date):
            update_event(event.event_id, True)
            # update_event_status_code(event.event_id, status_code=CLOSED)
            reminder(event.event_id, direction='in')  # 6.8

        # 6.10
        if event.type == 'obligation_sended' and (current_date - timedelta(days=5)) == event.reminder_date or (
                current_date - timedelta(
                days=5)) > event.reminder_date and event.event_id not in list_event_id_for_6_10:
            list_event_id_for_6_10.append(event.event_id)
            update_event(event.event_id, True)
            reminder_for_6_10(event.event_id)


while True:
    try:
        read()
    # except Exception as error:
    except:
        print(traceback.format_exc())
        # print(error)
    time.sleep(1)

# bot.polling()
