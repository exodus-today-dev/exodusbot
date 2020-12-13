# GREEN_BALL = '\U0001F7E2'
from models import read_user_language

GREEN_BALL = '\U00002705'  # Heavy Check Mark
# ORANGE_BALL = '\U0001F7E0'
ORANGE_BALL = '\U0001F506'  # High Brightness
# RED_BALL = '\U0001F534'
RED_BALL = '\U0001F198'  # sos

HEART_RED = '\U00002764'
HANDSHAKE = '\U0001F91D'
HELP = '\U0001F64F'

RIGHT_ARROW = '->'
LEFT_ARROW = '<-'
# PLUS = '\U00002795'
# MINUS = '\U00002796'
PLUS = '╋'
MINUS = '━'

MAN = '\U0001F464'
PEOPLES = '\U0001F465'
CREDIT_CARD = '\U0001F4B3'
MONEY_BAG = '\U0001F4B0'
FOOTPRINTS = '\U0001F463'
SPEECH_BALOON = '\U0001F4AC'
GLOBE = '\U0001F517'  # Globe with Meridians
GLOBE_NEW = '\U0001F310'  # Globe with Meridians
SPEAK_HEAD = '\U0001F5E3'  # Speaking Head In Silhouette
SPIRAL_CALENDAR = '\U0001F5D3'  # Spiral Calendar Pad
QUESTION = '\U00002753'  # Black Question Mark Ornament
LIKE = '\U0001F44D'  # Like
RUSSIAN = '\U0001F1F7'  # Russian flag
AMERICAN = '\U0001F1F8'  # American flag

START_TEXT = \
    {
        "ru":
            "Бот Эксодус - \n\
организация децентрализованной сетевой взаимопомощи.\n\n\
Выберите пояснение к использованию бота в меню",
        "en":
            "Bot Exodus - \n\
organization of decentralized network mutual assistance.\n\n\
Select an explanation for using the bot from the menu"
    }

TEXT_INSTRUCTIONS = \
    {
        "ru":
            f'*Добро пожаловать в Exodus!*\n\n\
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
\U0001f465 Участники - отвечает за просмотр своего профиля, работу с моей сетью и ее расширением, а также просмотр участников моей сети и неотвеченных запросов о помощи.',
        "en":
            "In procesing..."
    }

TEXT_ABOUT = \
    {
        "ru":
            "Бот Эксодус создает условия для создания референтной сети доверия участников, оказывающих безвозмездную " \
            "взаимную помощь с целью обеспечения базовых нужд и оказания экстренной помощи участникам.\n\n" \
            "Бот не является платежной платформой, он фиксирует потребность в помощи, ситуацию оказания помощи, " \
            "проявляет сеть участников, объединенных общими кругами заботы.\n\n" \
            "Бот позволяет звать на помощь нуждающимся своих друзей, этим расширяя референтную сеть доверия.\n\n" \
            f"Для каждого участника бот показывает список помогающих ему {PEOPLES}{RIGHT_ARROW}{MAN}, " \
            f"и список тех, кому он помогает {MAN}{RIGHT_ARROW}{PEOPLES}, а также его статус и текущую ситуацию сбора. " \
            f"Через оказания помощи большему числу участников происходит расширение вашей референтной сети доверия.\n\n" \
            f"Расчетный период работы бота один месяц. В конце месяца происходит переход в новый период. " \
            f"Не принявшие деятельного участия в помощи или не выполнившие своих обязательств выпадают из данной референтной сети доверия и взаимной помощи.\n\n" \
            f"В дальнейшем на основе референтных сообществ и их расширения могут возникать децентрализованные " \
            f"сети взаимного социального обеспечения, кооперативного взаимодействия, самодостаточной р2р экономики.",
        "en":
            "In procesing..."
    }
TEXT_CONVENTION = \
    {
        "ru":
"""
*Условныеобозначения в боте*

*Статус пользователя:*
✅ - я готов помогать участникам сети, мне сейчас помощь не требуется
🔆 - мне необходима ежемесячная поддержка, я могу помогать другим участникам сети
🆘 - мне требуется экстренная помощь в ограниченный срок

*Показатели сбора и оказания помощи:*
Расчетная единица в текущей версии бота USD
💰 - объем ежемесячной или экстренной помощи, задаётся в профиле при смене статуса, может корректироваться в профиле при необходимости.
❤️ - объем намерений. Намерение показывает готовность участников сети оказать помощь и позволяет сбалансировать объем этой помощи в конкретном случае (чем больше желающих помочь – тем меньше сумма каждого). Намерение может быть скорректировано или свободно отозвано. Переводится в обязательства по запросу или готовности. 
🤝 - объем обязательства. Это фиксация договоренности помочь, которую нельзя отозвать. Обязательства могут храниться до конца месячного периода или предъявляться к исполнению. 
👍 - исполненное обязательство. Исполнение подтверждается получателем помощи.
🙏🏻 - объем недостающей помощи. Уменьшается по мере перевода намерений в обязательства и их исполнения. Общая сумма намерений сопоставляется с объемом требуемой помощи. Участники сети, корректируя свои намерения, стремятся свести эту сумму к нулю.

*Как прочитать данные о пользователе:*
User Lastname 🔆 / 🔗Помочь / 💬 обо мне www.mypage.info / 💳 PayPal User.blabla@gmail.com
2 👥 -> 👤 (75.0 ❤️ / 475.0 🙏)
👤 -> 2 👥: 20.0 ❤️ / 10.0 🤝

Пользователь User Lastname в оранжевом статусе, ему требуется ежемесячная регулярная поддержка, он может и помогать, и принимать помощь. Чтобы помочь ему, нужно кликнуть на ссылку 🔗Помочь или скопировать эту ссылку и переслать друзьям, приглашая их участвовать.
Узнать подробнее о ситуации пользователя и основаниях для его сбора можно по ссылке 💬обо мне www.mypage.info
Оказать помощь можно по указанным реквизитам

Два участника сети помогают этому пользователю сейчас, объем их намерений равен 75 и это меньше требуемой для закрытия сбора суммы в 475 USD.
Пользователь сам помогает двум участникам общей референтной сети, сумма его объявленных намерения равна 20, а объем обязательств равен 10.
""",
        "en":
           """
* Symbols in the bot:*

*User status:*
✅ - I am ready to help network members, I don't need help now
🔆 - I need monthly support, I can help other network members
🆘 - I need emergency assistance for a limited time

*Collection and delivery rates:*
Unit of account in the current version of the bot USD
💰 - the amount of monthly or emergency assistance, set in the profile when changing the status, can be adjusted in the profile if necessary.
❤️ - volume of intentions. The intention shows the willingness of the network participants to provide assistance and allows you to balance the amount of this assistance in a particular case (the more willing to help - the less the amount of each). The intention can be adjusted or withdrawn freely. Translated into on-demand or readiness obligations.
🤝 - the amount of the obligation. This is a fixation of an agreement to help that cannot be revoked. Liabilities can be kept until the end of the month period or presented for execution.
👍 - fulfilled obligation. Execution is confirmed by the beneficiary.
🙏🏻 - amount of missing aid. Decreases as intentions are translated into obligations and their fulfillment. The total amount of intentions is compared with the amount of assistance required. The network participants, adjusting their intentions, seek to reduce this amount to zero.

*How to read user data:*
User Lastname 🔆 / 🔗Help / 💬 about me www.mypage.info / 💳 PayPal User.blabla@gmail.com
2 👥 -> 👤 (75.0 ❤️ / 475.0 🙏)
👤 -> 2 👥: 20.0 ❤️ / 10.0 🤝

User Lastname is orange, needs monthly regular support, and can both help and accept help. To help him, you need to click on the 🔗Help link or copy this link and send it to friends, inviting them to participate.
You can learn more about the user's situation and the grounds for collecting it by following the link about me www.mypage.info
You can provide assistance at the specified details.

Two network participants are helping this user now, the volume of their intentions is 75 and this is less than the 475 USD required to close the collection.
The user himself helps two participants in the common reference network, the sum of his declared intentions is 20, and the volume of obligations is 10.
"""
    }
TEXT_MENU = \
    {
        "ru":
            f"*Главное меню бота Эксодус*\n\n" \
            f"{MAN}*Профиль*\n" \
            f"Статус - указать актуальный статус и данные для помощи - сумму сбора и срок для экстренного сбора.\n" \
            f"{SPEECH_BALOON} Обо мне - можно кратко описать и дать ссылку на обсуждение своей ситуации (по желанию, 180 знаков).\n" \
            f"{CREDIT_CARD}Реквизиты - можно задать реквизиты для оказания помощи (по умолчанию - спросить лично).\n" \
            f"{GLOBE_NEW} RU/ENG - выбрать язык бота русский / английский.\n" \
            f"{FOOTPRINTS}Выйти из бота - удалить все свои сведения из бота.\n\n" \
            f"*{PEOPLES} Участники*\n" \
            f"Моя сеть {PEOPLES} 3 - количество и список всех участников референтной сети и ситуация их сбора:\n" \
            f"  ID1 Name1 {GREEN_BALL} - участник не нуждается в помощи.\n" \
            f"  ID2 Name2 {ORANGE_BALL} 50{HEART_RED}/500{HELP}🏻 - участнику требуется регулярная поддержка, сумма намерений в его пользу 50USD, объем недостающей помощи 500USD.\n" \
            f"  ID3 Name3 {RED_BALL}  500{HELP} / 10 дней участник проводит экстренной сбор, ему необходимо собрать 500USD в течение 10 дней. Экстренный сбор закрывается только обязательствами.\n\n" \
            f"При указании ID участника можно увидеть:\n" \
            f"  Данные профиля этого участника, включая ссылку на обсуждение его ситуации,  реквизиты для помощи ему, ссылку для оказания помощи.\n" \
            f"  Сеть {PEOPLES} Username - список всех, включенных в референтную сеть этого пользователя.\n" \
            f"  Username{RIGHT_ARROW}{PEOPLES} - список всех участников сети, кому этот пользователь помогает.\n" \
            f"  {PEOPLES}{RIGHT_ARROW}Username - список участников, кто помогает этому пользователю. Если вы тоже ему помогаете, то увидите всю ситуацию по сбору; если еще не помогаете, то доступен только общий список помогающих.\n" \
            f"{GLOBE} Помочь Username - реферальная ссылка для помощи этому пользователю бота, " \
            f"которую можно разослать друзьям. При клике на ссылку происходит переход в бота и " \
            f"появляется запрос о возможности помощи выбранному пользователю.\n\n" \
            f"*Расширить сеть* - производит автоматическое расширение вашей сети после включения в сеть новых участников, в отношении которых вы проявили намерение помочь. Вы начинаете видеть других участников сети, которые также помогают выбранному вами пользователю бота. Таким образом формируется децентрализованная автономная сеть, связанная отношениями открытой добровольной и безвозмездной помощи участников друг другу, невидимая извне.\n\n" \
            f"🗓*Органайзер* - управление намерениями и обязательствами:\n" \
            f"3{HEART_RED}/ 1🤝 -> {MAN} - показывает число актуальных намерений и обязательств в мою пользу, " \
            f"позволяет формировать запросы на перевод {HEART_RED} в {HANDSHAKE} и исполнение сохраненных ранее обязательств.\n" \
            f"{MAN}->2{HEART_RED} / 2🤝 - показывает число актуальных намерений и обязательств в пользу " \
            f"других участников сети, позволяет управлять ими:  для намерений{HEART_RED} -  отзывать, " \
            f"корректировать сумму, переводить в обязательства;\n" \
            f"  для обязательств 🤝 - подтвердить исполнение, напомнить позже.\n" \
            f"3/450{LIKE} ->{MAN}->2/240{LIKE} - архив исполненных обязательств в вашу пользу и ваших " \
            f"в пользу других участников сети (общее число/сумма осуществленных переводов в отчетный период).\n\n" \
            f"{MAN}-> 3 {PEOPLES} Список всех, кому вы помогаете в текущий момент, с возможностью просмотреть их данные по указанному ID.\n" \
            f"2 {PEOPLES}{RIGHT_ARROW}{MAN} Список всех, кто помогает вам, с возможностью посмотреть их данные по указанному ID.\n\n" \
            f"🤝->{LIKE} 2->{MAN}->2 список всех обязательств, которые отправителем отмечены как исполненные, а получателем еще не подтверждены. Дают возможность отметить исполнение обязательства в свою пользу или направить уведомление-напоминание с просьбой подтвердить исполнение.\n\n" \
            f"*{QUESTION}FAQ* - описывает основные возможности работы бота.\n\n" \
            f"*{SPEECH_BALOON}Чат поддержки* - ссылка на канал с объяснениями работы системы Эксодус. Возможность задать вопрос в техподдержку, если что-то в работе бота не ясно, сообщить об ошибках, высказать свои замечания и предложения о дальнейшем совершенствовании бота.\n\n" \
            f"*{GLOBE}Помочь* - показывает список всех участников референтной сети, у которых сейчас идет активный сбор, с формированием реферальной ссылки для помощи каждому из них.",
        "en":
            """
*Menu of the Exodus bot*

👤*Profile*
Status - indicate the current status and data for assistance - the amount of the fee and the deadline for the emergency fee.
💬About me - you can briefly describe and give a link to a discussion of your situation (optional, 180 characters).
💳Details - you can set the requisites for assistance (by default - ask in person).
🌐RU / ENG - select the bot language Russian / English.
👣 Log out - remove all your information from the bot.


*👥 Participants*
My network 👥 3 - the number and list of all members of your reference network and the situation of their collection:
ID1 Name1 ✅ - the participant does not need help.
ID2 Name2 🔆 50❤️ / 500🙏🏻 - the participant needs regular support, the amount of intentions in his favor is 50USD, the amount of missing aid is 500USD.
ID3 Name3 🆘 500🙏🏻 / 10 days - the participant conducts an emergency fee, he needs to collect 500USD within 10 days. The emergency fee is closed only by obligations.

When specifying the participant ID, you can see:
Profile data of this participant, including a link to a discussion of his situation, details to help him, a link to help.
Network 👥 Username - a list of everyone included in this user's reference network.
Username-> 👥 - a list of all network members whom this user helps.
👥-> Username - a list of members who help this user. If you also help him, you will see the whole collection situation; if you are not helping yet, only the general list of helpers is available.
🔗Help Username - referral link to help this bot user, which can be sent to friends. When you click on the link, you go to the bot and a request appears about the possibility of helping the selected user.

*Expand network* - automatically expands your network after adding new members to the network for whom you have expressed your intention to help. You start to see other members of the network who are also helping the bot user of your choice. Thus, a decentralized autonomous network is formed, connected by relations of open voluntary and gratuitous assistance of participants to each other, invisible from the outside.


🗓*Organizer* - management of intentions and obligations:
3❤️ / 1🤝 -> 👤 shows the number of actual intentions and obligations in your favor, allows you to form requests for transferring ❤️ to 🤝 and fulfillment of previously saved obligations
👤-> 2❤️ / 2🤝 shows the number of actual intentions and obligations in favor of other network participants, allows you to manage them:
for intentions❤️ - to withdraw, adjust the amount, transfer into liabilities;
for obligations 🤝 - confirm performance, remind later.
3 / 450👍 -> 👤-> 2 / 240👍 - archive of fulfilled obligations in your favor and yours in favor of other network members (total number / amount of transfers made during the reporting period).

👤-> 3 👥 A list of everyone you are helping at the moment, with the ability to view their data by the specified ID
2 👥-> 👤 A list of everyone who helps you, with the ability to view their details by the specified ID

🤝-> 👍 2-> 👤-> 2 a list of all obligations that are marked as fulfilled by the sender, but the recipient has not yet confirmed. They give the opportunity to mark the fulfillment of the obligation in their favor or send a reminder notification with a request to confirm the fulfillment.

*❓FAQ* - describes the main features of the bot.

*💬Support chat* - link to the channel with explanations of the Exodus system. Possibility to ask a question to technical support if something in the bot's work is not clear, to report bugs, to express your comments and suggestions on further improving the bot.

🔗*Help* - shows a list of all members of the reference network who are currently actively collecting, with the formation of a referral link to help each of them."""
    }

TEXT_HOW_START = \
    {
        "ru":
            f"*Как начать работу в боте.*\n\n" \
            f"*Сценарий 1.* Вам нужна помощь. Вы ещё не входите ни в чью сеть.\n\n" \
            f"1. Вы регистрируетесь в боте по стартовой ссылке @exodus\_commitbot." \
            f"По умолчанию статус при регистрации {GREEN_BALL}.\n\n" \
            f"2.  Рекомендуем описать свою ситуацию и обстоятельства, обосновывающие необходимость поддержки " \
            f"на любом удобном для коммуникации ресурсе (чат, мессенджер, соцсеть и тп.)." \
            f"Ссылку на этот ресурс сохраняете в данных своего профиля.\n\n" \
            f"3. Заполняете данные своего профиля - меняете статус на {ORANGE_BALL} регулярная помощь " \
            f"или {RED_BALL} - экстренная помощь. Указываете необходимую сумму сбора, " \
            f"ссылку на обсуждение, реквизиты для помощи.\n\n" \
            f"4. Теперь можно в пункте главного меню {GLOBE}Позвать сгенерить ссылку " \
            f"для помощи и разослать её друзьям. Друзья, готовые вам помочь, уже попадают в вашу сеть.\n\n" \
            f"*Сценарий 2.*  Вы хотите пригласить друга, чтобы помогать ему. " \
            f"Вам самому помощь не требуется. Вы объясняете другу, что сделать.\n\n" \
            f"Ваш друг действует по сценарию 1, присылает вам ссылку для помощи себе, " \
            f"вы отвечаете да и теперь вы в одной сети. " \
            f"После этого вы можете приглашать других своих знакомых помогать своему другу.\n\n" \
            f"*Сценарий 3.* Вы попадаете в бот по чьей-то ссылке-приглашению, " \
            f"присоединяясь к локальной сети своего друга.",
        "en":
            "In procesing..."
    }

TEXT_CASE = \
    {
        "ru":
            f"*Возможные кейсы для использования бота Exodus*\n\n" \
            f"*Обеспечение базового дохода иждивенцам:* дети, родители, инвалиды, заболевшие, " \
            f"семьи в тяжёлой жизненной ситуации, временно потерявшие работу и тп." \
            f"Сообщество может взять на себя адресную заботу о таких людях. " \
            f"При этом помощь оказывается адресно, тем соседям и друзьям, " \
            f"которых лично знаем или которых лично знают люди, которым доверяем. " \
            f"Люди попадают в круг внимания и заботы, а не в безразличное и безличное обеспечение социальными службами. " \
            f"Личное соучастие исключает сборы мошенниками. " \
            f"Распределенное внимание снижает нагрузку на каждого заботящегося. " \
            f"Сообщество стремится не держать человека в позиции только получающего, " \
            f"но помогает выйти из тяжёлой ситуации связями и компетенциями. " \
            f"Получатели регулярной помощи также посильно участвуют во взаимном обмене.\n\n" \
            f"*Базовый доход для творцов и деятелей немонетизируемых профессий.* " \
            f"В условиях кризиса многие творцы музыканты, художники, писатели оказались в ограниченных условиях. " \
            f"Не все из них смогли адаптироваться к онлайн среде. Их поклонники привыкли дарить цветы или покупать билеты. " \
            f"Тогда как многие сейчас еле сводят концы с концами. " \
            f"Платформы типа Патреона значительную часть передаваемых средств тратят на самообслуживание. " \
            f"Эксодус помогает сделать формат сбора базового дохода для творцов простым, прямым и прозрачным. " \
            f"А творец получает возможность свободно творить и не думать о хлебе насущном или путях продажи своего труда.\n\n" \
            f"*Представители некоммерческого сектора.* Сейчас деятельность многих НКО зависит от грантов. " \
            f"Но гранты имеют ограничение на зарплаты сотрудников в них. Это одна из больных точек " \
            f"некоммерческого сектора, в котором считается, что люди, занимающиеся благотворительностью, " \
            f"должны делать это как волонтёры и в свободное от основной работы время." \
            f"Если сообщество считает, что труд этих людей полезен, " \
            f"то можно уйти от зависимости от грантов для обеспечения непрерывности такой работы.\n\n" \
            f"*Сбор на общие мероприятия.* Используя бот Эксодус, можно сделать прозрачным процесс сбора средств " \
            f"на общие мероприятия, будь это выезд на шашлыки, ежемесячная работа клуба по интересам, " \
            f"творческий фестиваль. Бот показывает намерения всех заинтересованных в этом событии, " \
            f"позволяет динамически регулировать суммы сбора. Также можно увидеть, " \
            f"что какая-то инициатива не собрала достаточного числа интересантов и " \
            f"отказаться от её реализации до того, как начать отдавать реальные средства.\n\n" \
            f"*Экстренные сборы.* Свадьба, похороны, покупка машины, строительство дома, обучение детей. " \
            f"Пожар, авария, лечение. Стартовый капитал. " \
            f"Иногда людям требуется собрать достаточно крупную сумму в ограниченное время. " \
            f"Эксодус позволяет оповестить друзей о такого рода нужде и получить разовую безвозмездную поддержку." \
            f"Чем большему числу людей пользователь помогал ранее, тем большее число друзей " \
            f"придёт к нему на помощь в нужный момент. " \
            f"Предполагается, что это система взаимного страхования, " \
            f"и что получивший помощь сегодня точно так же отзовётся на помощь товарищам завтра.\n\n" \
            f"*Благотворители и меценаты*, используя бот Эксодус, получают возможность выбирать круги своей заботы, " \
            f"оказывать помощь тому, кто им более близок, находить единомышленников, оптимально распределять " \
            f"свои средства по большему кругу нуждающихся, сокращать издержки на посредников и непроизводительные траты.\n\n" \
            f"*Учёт оказанных безвозмездных услуг.* Взаимная помощь может быть оказана и в немонетарной форме -" \
            f" консультация, массаж, урок, ремонт, транспортные услуги, предоставление помещения и тд. " \
            f"Все эти формы помощи можно перевести в денежный эквивалент и учесть как исполненное обязательство. " \
            f"Это помогает включить в продуктивные взаимодействия людей, у которых нет денежных средств, " \
            f"начать ценить 'бесплатные' услуги, стимулировать немонетарные обмены услугами, " \
            f"выводя людей из зоны вынужденной беспомощности от отсутствия денег.\n\n" \
            f"*Эксодус* по умолчанию предполагает формат прямого безвозмездного дара от " \
            f"физического лица физическому лицу." \
            f"Но каждый просящий помощи и оказывающий её могут договариваться об удобных форматах её оказания " \
            f"и форме расчётов, при том, что непосредственные расчёты находятся за пределами бота.",
        "en":
            "In procesing..."
    }

TEXT_SUM_DIGIT = {'ru': 'Сумма должна быть только в виде цифр и больше 0',
                  'en': 'The amount must only be in digits and must be greater than 0'}

TEXT_NUMBER_DIGIT = {'ru': 'Номер должен быть в виде числа:',
                  'en': 'The number must be in the form of a digit:'}

TEXT_NOT_FIND = {'ru': 'Введённый номер не соовпадает с существующими',
                  'en': 'The entered number does not match the existing ones'}

INPUT_NUMBER_USER = {
    'ru':
        'Введите номер Участника, чтобы посмотреть подробную информацию:',
    'en':
        'Enter the Member number to view more information:'
}


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


def exception_message(message):
    lang = read_user_language(message.chat.id)
    if lang == "ru":
        msg = "Пошло что-то не так. Попробуйте снова или нажмите /start"
    else:
        msg = "Something went wrong. Try again or press /start"
    return msg
