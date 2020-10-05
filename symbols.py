#GREEN_BALL = '\U0001F7E2'
GREEN_BALL = '\U00002705' # Heavy Check Mark
#ORANGE_BALL = '\U0001F7E0'
ORANGE_BALL = '\U00002734' # Orange Star
#RED_BALL = '\U0001F534'
RED_BALL = '\U0001F198' # sos

HEART_RED = '\U00002764'
HANDSHAKE = '\U0001F91D'
HELP = '\U0001F64F'

RIGHT_ARROW = '->'
LEFT_ARROW = '<-'
# PLUS = '\U00002795'
# MINUS = '\U00002796'
PLUS = '╋'
MINUS = '━'

PEOPLES = '\U0001F465'
CREDIT_CARD = '\U0001F4B3'
FOOTPRINTS = '\U0001F463'
SPEECH_BALOON = '\U0001F4AC'


START_TEXT = "Бот Эксодус - \n\
организация децентрализованной сетевой взаимопомощи.\n\n\
О чем вы хотите узнать?"

TEXT_INSTRUCTIONS = f'*Добро пожаловать в Exodus!*\n\n\
Как только вы присоединитесь к сети, Вам необходимо выбрать статус.\n\n\
Зелёный статус {GREEN_BALL} - сообщает о том, что вы готовы помогать участникам сети.\n\
Оранжевый статус {ORANGE_BALL} - сообщает участникам сети, что вам необходима ежемесячная денежная поддержка.\n\
Сигнал о помощи {RED_BALL} можно выбрать после присоединения к сети. Он означает, что Вам требуется срочная помощь при возникновении экстренной ситуации.\n\n\
*Основные понятия*\n\
Статус - Ваше текущее состояние. Сигнализирует участникам сети о вашей готовности помочь или принять помощь.\n\
Намерение {HEART_RED} - изъявление желания помогать участнику сети.\n\
Обязательство {HANDSHAKE} - следующая стадия намерения. Сообщает участнику, который нуждается в помощи, что вы точно готовы помочь участнику сети.\n\
{PLUS} - в контексте означает "В мою пользу"\n\
{MINUS} - в контексте означает "В пользу других"\n\n\
*Пункты меню*\n\
\U0001f4ca Кошелек - отвечает за совершение операций между участниками твоей сети;\n\
\U0001f527 Настройки - отвечает за смену твоего статуса, редактировании ссылки на чат и работу с реквизитами;\n\
\U0001f465 Участники - отвечает за просмотр своего профиля, работу с моей сетью и ее расширением, а также просмотр участников моей сети и неотвеченных запросов о помощи.'

TEXT_PURPOSE = "Цель:\n- распределение имеющихся средств доноров среди максимального количества нуждающихся с формированием сети доверия невидимой извне,\
- развитие прямой кооперации и любых проектов имеющих актуальность для участников,\
- возникновение децентрализованной сети взаимного социального обеспечения и самодостаточной р2р экономики."

TEXT_METHOD = f"Способ:\nТелеграм бот @exodus_commitbot, позволяющий регистрировать и управлять записями о финансовых намерениях " \
              "и обязательствах участников референтных сообществ. Бот не является платежным инструментом - " \
              "исполнение взаимных финансовых обязательств осуществляется любыми способами вне его. " \
              "Бот позволяет участникам оставаться невидимыми для внешнего мира - его задача фиксировать " \
              "договоренности участников, разделив таким образом учет от реальной деятельности." \
              "\n\nБот дает возможность пользователю зарегистрироваться, зафиксировать статус " \
              f"(донор{GREEN_BALL}, постоянно нуждающийся{ORANGE_BALL}), уведомить о необходимой сумме регулярной финансовой помощи, " \
              f"уведомить о сумме регулярного (ежемесячного) намерения{HEART_RED} в отношении конкретного нуждающегося " \
              f"либо донора, отзывать намерения, исполнять обязательства{HANDSHAKE}, уведомлять о случаях связанных " \
              "с потребностью в разовой помощи (сменой статуса), уведомлять о случае ущерба других участников " \
              "совместных договоренностей а также формировать список всех кто связан общим участием в помощи другим."

TEXT_PRINCIPS = f"Принципы:\n\
1) Намерение{HEART_RED} может быть отозвано в любой момент без объявления причины.\n\
2) Обязательство{HANDSHAKE} взятое из добровольного намерения должно быть исполнено, неисполненное обязательство фиксируется в записи и формирует репутацию участника."

TEXT_GLOSSARY = f'Глоссарий:\n\n\
1) Статус\n\
{GREEN_BALL} - участник обеспечен базовыми нуждами\n\
{ORANGE_BALL} - участник нуждается в регулярной ежемесячной помощи\n\
{RED_BALL} - участник просит помощи в чрезвычайной ситуации - сумма, дата.\n\n\
2) Намерение{HEART_RED} - запись суммы уведомляющая о готовности регулярно (ежемесячно) помогать конкретному участнику. ' \
                'Намерение может быть отозвано в любой момент без объяснения причин и записи. ' \
                'В тот момент когда участник отзывает намерение он теряет возможность видеть тех участников ' \
                f'которые были объединены общим объектом помощи.\n\n\
3) Обязательство{HANDSHAKE} - запись суммы уведомляет участника о готовности произвести платеж после получения требования ' \
                'со стороны того в чью пользу зафиксировано обязательство. Обязательство должно быть исполнено. ' \
                'В случае неисполнения запись фиксируется и все участники информируются об этом.\n\n\
 4) Базовые нужды: то без чего человек не может обойтись - есть, пить, крыша над головой. одежда и тд.\n\n\
 5) Моя сеть - участники связанные взаимопомощью общим для них нуждающимся.'

TEXT_HOW_WORK = f'Как это работает:\n\
При регистрации в системе участник выбирает себе статус : {GREEN_BALL} (донор) либо {ORANGE_BALL} ' \
                f'(с указанием необходимой ежемесячной суммы). При формировании этой суммы {ORANGE_BALL} ' \
                'исходит из того, что ему будет достаточно для обеспечения базовых нужд.' \
                f'\n\nДоноры уведомляют фиксацией намерения{HEART_RED} в отношении приглашенного нуждающегося других доноров и ' \
                'через "перекрестное" финансирование "проявляется" сетка доноров и нуждающихся. ' \
                'Участники такой сети формируют "пул" взаимных намерений - по сути предварительно договариваются ' \
                'о том, как намереваются участвовать в покрытии ущерба другого, если возникнет необходимость. ' \
                'С этого момента каждый участник становится застрахованным от рисков в размере совокупных намерений всех.'


def get_status(text):
    if text == "green":
        status = GREEN_BALL
    elif text == "orange":
        status = ORANGE_BALL
    elif 'red' in text:
        status = RED_BALL
    else:
        status = ""
    return status
