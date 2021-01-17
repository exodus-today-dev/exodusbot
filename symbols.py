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
"""
Использование бота позволяет формировать список участников взаимной помощи, что является необходимым условием возникновения децентрализованной сети доверия.

Выберите пояснение к использованию бота.
""",
        "en":
"""
Using the bot allows you to create a list of participants in mutual assistance, which is a necessary condition for the emergence of a decentralized network of trust.

Select an explanation for using the bot.
"""
    }

TEXT_INSTRUCTIONS = \
    {
        "ru":
            f'<b>Добро пожаловать в Exodus!</b>\n\n\
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
            """
Бот Эксодус обеспечивает технический  учёт и управление взаимными договорённостями участников референтной сети по оказанию взаимной помощи и поддержки. 

Бот имеет двухуровневый механизм баланса помощи между пулом участников через систему свободно корректируемых намерений и обязательных к исполнению обязательств.  Таким образом можно оптимизировать распределение добровольной помощи между участниками сети. Учет транзакций осуществляется в финансовом эквиваленте, в данной версии бота мерой является USD.

Бот не является платежной платформой, он фиксирует потребность в помощи, ситуацию оказания помощи, проявляет сеть участников, объединенных общими намерениями поддержки.   Эксодус по умолчанию предполагает формат прямого безвозмездного дара от физического лица физическому лицу. Но каждый просящий помощи и оказывающий её могут договариваться об удобных форматах её оказания и форме расчётов, при том, что непосредственные договоренности и расчёты находятся за пределами бота.

Для каждого пользователя бот показывает список помогающих ему 👥->👤 и список тех, кому он помогает👤->👥, а также их статус и текущую ситуацию сборов. Бот позволяет звать на помощь нуждающимся своих друзей.  Референтная локальная сеть доверия растет через систему реферальных ссылок по принципу «друг моего друга - мой друг». Расширение сети происходит в случае «встречи» участников локальных референтных сетей через общие ситуации оказания помощи.

Расчетный период работы бота один месяц. В конце месяца происходит переход в новый период. Не принявшие деятельного участия в помощи или не выполнившие своих обязательств выпадают из данной референтной сети доверия и взаимной помощи. 

Основные принципы взаимодействия в боте между участниками сети - помощь оказывается непосредственно, распределенно, децентрализованно, добровольно, безущербно, взаимовыгодно, открыто для участников референтной сети. 

Формализация  актов взаимной помощи в едином эквиваленте является  условием для появления сети доверия, не имеющей численных ограничений, границ и видимой формы.

Бот позволяет создавать достаточно большие по мощности распределенные сети взаиного доверия, невидимые извне для тех, кто в отношения взаимной помощи не включен. Таким образом возникает альтернативная система взаимного социального страхования - основа новых децентрализованных социальных отношений. 

В дальнейшем на основе референтных сообществ и их расширения могут возникать децентрализованные сети взаимного социального обеспечения, кооперативного взаимодействия, самодостаточной р2р экономики.

Бот работает на русском и английском языке.
            """,
        "en":
            """
Bot Exodus provides technical accounting and management of mutual agreements of participants in the reference network for the provision of mutual assistance and support.

The bot has a two-tier mechanism for balancing assistance between a pool of participants through a system of freely adjustable intentions and binding obligations. Thus, it is possible to optimize the distribution of voluntary assistance among network participants. Transactions are recorded in financial terms, in this version of the bot, the measure is USD.

The bot is not a payment system; it records the need for assistance, the situation of assistance, and displays a network of participants united by common support intentions. Exodus by default assumes the format of a direct gratuitous gift from an individual to an individual. But everyone who asks for help and provides it can agree on convenient formats for its provision and the form of payments, despite the fact that direct agreements and calculations are outside the bot.

For each user, the bot shows a list of helpers 👥-> 👤 and a list of those it helps 👥-> 👥, as well as their status and current collection situation. The bot allows you to call your friends for help. The local referral network of trust grows through the system of referral links on the principle ""my friend's friend is my friend."" The expansion of the network occurs in the event of a ""meeting"" of participants in local reference networks through general situations of assistance.

The estimated period of work of the bot is one month. At the end of the month, there is a transition to a new period. Those who did not take an active part in assistance or who did not fulfill their obligations fall out of this reference network of trust and mutual assistance.

The basic principles of interaction in a bot between network participants - assistance is provided directly, distributed, decentralized, voluntarily, harmlessly, mutually beneficial, open to participants in the reference network.

Formalization of acts of mutual assistance in a single equivalent is a precondition for the emergence of a web of trust that has no numerical limitations, boundaries and visible form.

The bot allows you to create large enough distributed networks of mutual trust, invisible from the outside for those who are not involved in mutual assistance relations. Thus, an alternative system of mutual social insurance arises - the basis of new decentralized social relations.

In the future, on the basis of reference communities and their expansion, decentralized networks of mutual social security, cooperative interaction, and a self-sufficient p2p economy may arise.

The bot works in Russian and English.
            """
    }
TEXT_CONVENTION = \
    {
        "ru":
"""
<b>Условные обозначения в боте</b>

<b>Статус пользователя:</b>
✅ - я готов помогать участникам сети, мне сейчас помощь не требуется
🔆 - мне необходима ежемесячная поддержка, я могу помогать другим участникам сети
🆘 - мне требуется экстренная помощь в ограниченный срок

<b>Показатели сбора и оказания помощи:</b>
Расчетная единица в текущей версии бота USD
💰 - объем ежемесячной или экстренной помощи, задаётся в профиле при смене статуса, может корректироваться в профиле при необходимости.
❤️ - объем намерений. Намерение показывает готовность участников сети оказать помощь и позволяет сбалансировать объем этой помощи в конкретном случае (чем больше желающих помочь – тем меньше сумма каждого). Намерение может быть скорректировано или свободно отозвано. Переводится в обязательства по запросу или готовности. 
🤝 - объем обязательства. Это фиксация договоренности помочь, которую нельзя отозвать. Обязательства могут храниться до конца месячного периода или предъявляться к исполнению. 
👍 - исполненное обязательство. Исполнение подтверждается получателем помощи.
🙏🏻 - объем недостающей помощи. Уменьшается по мере перевода намерений в обязательства и их исполнения. Общая сумма намерений сопоставляется с объемом требуемой помощи. Участники сети, корректируя свои намерения, стремятся свести эту сумму к нулю.

<b>Как прочитать данные о пользователе:</b>
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
<b> Symbols in the bot:</b>

<b>User status:</b>
✅ - I am ready to help network members, I don't need help now
🔆 - I need monthly support, I can help other network members
🆘 - I need emergency assistance for a limited time

<b>Collection and delivery rates:</b>
Unit of account in the current version of the bot USD
💰 - the amount of monthly or emergency assistance, set in the profile when changing the status, can be adjusted in the profile if necessary.
❤️ - volume of intentions. The intention shows the willingness of the network participants to provide assistance and allows you to balance the amount of this assistance in a particular case (the more willing to help - the less the amount of each). The intention can be adjusted or withdrawn freely. Translated into on-demand or readiness obligations.
🤝 - the amount of the obligation. This is a fixation of an agreement to help that cannot be revoked. Liabilities can be kept until the end of the month period or presented for execution.
👍 - fulfilled obligation. Execution is confirmed by the beneficiary.
🙏🏻 - amount of missing aid. Decreases as intentions are translated into obligations and their fulfillment. The total amount of intentions is compared with the amount of assistance required. The network participants, adjusting their intentions, seek to reduce this amount to zero.

<b>How to read user data:</b>
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
            f"<b>Главное меню бота Эксодус</b>\n\n" \
            f"{MAN}<b>Профиль</b>\n" \
            f"Статус - указать актуальный статус и данные для помощи - сумму сбора и срок для экстренного сбора.\n" \
            f"{SPEECH_BALOON} Обо мне - можно кратко описать и дать ссылку на обсуждение своей ситуации (по желанию, 180 знаков).\n" \
            f"{CREDIT_CARD}Реквизиты - можно задать реквизиты для оказания помощи (по умолчанию - спросить лично).\n" \
            f"{GLOBE_NEW} RU/ENG - выбрать язык бота русский / английский.\n" \
            f"{FOOTPRINTS}Выйти из бота - удалить все свои сведения из бота.\n\n" \
            f"<b>{PEOPLES} Участники</b>\n" \
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
            f"<b>Расширить сеть</b> - производит автоматическое расширение вашей сети после включения в сеть новых участников, в отношении которых вы проявили намерение помочь. Вы начинаете видеть других участников сети, которые также помогают выбранному вами пользователю бота. Таким образом формируется децентрализованная автономная сеть, связанная отношениями открытой добровольной и безвозмездной помощи участников друг другу, невидимая извне.\n\n" \
            f"🗓<b>Органайзер</b> - управление намерениями и обязательствами:\n" \
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
            f"<b>{QUESTION}FAQ</b> - описывает основные возможности работы бота.\n\n" \
            f"<b>{SPEECH_BALOON}Чат поддержки</b> - ссылка на канал с объяснениями работы системы Эксодус. Возможность задать вопрос в техподдержку, если что-то в работе бота не ясно, сообщить об ошибках, высказать свои замечания и предложения о дальнейшем совершенствовании бота.\n\n" \
            f"<b>{GLOBE}Помочь</b> - показывает список всех участников референтной сети, у которых сейчас идет активный сбор, с формированием реферальной ссылки для помощи каждому из них.",
        "en":
            """
<b>Menu of the Exodus bot</b>

👤<b>Profile</b>
Status - indicate the current status and data for assistance - the amount of the fee and the deadline for the emergency fee.
💬About me - you can briefly describe and give a link to a discussion of your situation (optional, 180 characters).
💳Details - you can set the requisites for assistance (by default - ask in person).
🌐RU / ENG - select the bot language Russian / English.
👣 Log out - remove all your information from the bot.


<b>👥 Participants</b>
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

<b>Expand network</b> - automatically expands your network after adding new members to the network for whom you have expressed your intention to help. You start to see other members of the network who are also helping the bot user of your choice. Thus, a decentralized autonomous network is formed, connected by relations of open voluntary and gratuitous assistance of participants to each other, invisible from the outside.


<b>Organizer</b> - management of intentions and obligations:
3❤️ / 1🤝 -> 👤 shows the number of actual intentions and obligations in your favor, allows you to form requests for transferring ❤️ to 🤝 and fulfillment of previously saved obligations
👤-> 2❤️ / 2🤝 shows the number of actual intentions and obligations in favor of other network participants, allows you to manage them:
for intentions❤️ - to withdraw, adjust the amount, transfer into liabilities;
for obligations 🤝 - confirm performance, remind later.
3 / 450👍 -> 👤-> 2 / 240👍 - archive of fulfilled obligations in your favor and yours in favor of other network members (total number / amount of transfers made during the reporting period).

👤-> 3 👥 A list of everyone you are helping at the moment, with the ability to view their data by the specified ID
2 👥-> 👤 A list of everyone who helps you, with the ability to view their details by the specified ID

🤝-> 👍 2-> 👤-> 2 a list of all obligations that are marked as fulfilled by the sender, but the recipient has not yet confirmed. They give the opportunity to mark the fulfillment of the obligation in their favor or send a reminder notification with a request to confirm the fulfillment.

<b>❓FAQ</b> - describes the main features of the bot.

<b>💬Support chat</b> - link to the channel with explanations of the Exodus system. Possibility to ask a question to technical support if something in the bot's work is not clear, to report bugs, to express your comments and suggestions on further improving the bot.

🔗<b>Get help</b> - shows a list of all members of the reference network who are currently actively collecting, with the formation of a referral link to help each of them."""
    }

TEXT_HOW_START = \
    {
        "ru":
"""
<b>Как начать работу в боте и добавить участников в свою сеть?</b>

Рост сети начинается с того, кому нужна помощь. 

<b>Сценарий 1.</b> Вам нужна помощь. Вы ещё не входите ни в чью сеть. 
1. Вы регистрируетесь в боте по стартовой ссылке https://t.me/exodus_commitbot.  По умолчанию статус при регистрации ✅. 
2. Решите, куда смогут обратиться пользователи бота, чтобы связаться с вами или лучше узнать вашу ситуацию - это может быть социальная сеть,  чат в мессенджере, сайт и тд - любой удобный вам ресурс. 
3. Заполните данные своего 👤Профиля: 
✅Статус - поменяйте статус на 🔆-регулярная помощь или 🆘-экстренная помощь, укажите необходимую сумму ежемесячного или экстренного сбора. 
💬Обо мне - вы можете ввести краткие сведения о себе и ссылку на обсуждение (по желанию, ограничение 180 знаков). 
💳Реквизиты - вы можете задать реквизиты для оказания финансовой помощи (банковская карта, платежная система, ссылка на сервис сбора и тд. По умолчанию спросить лично). 
4. Теперь можно в пункте главного меню 🔗Помочь  создать реферальную ссылку для помощи и разослать её друзьям. 
Друзья, готовые вам помочь, попадают в вашу сеть и могут также пользоваться ботом для взаимной помощи.

<b>Сценарий 2.</b>  Вы хотите организовать помощь другу по принципам системы Эксодус. При этом вам самому помощь не требуется. 
1. Вы с другом/друзьями договариваетесь о такой модели взаимной помощи. Вы объясняете другу, что ему сделать, чтобы начать создавать автономную референтную сеть помощи ему. 
2. Ваш друг действует по сценарию, описанному выше и присылает вам и своим друзьям ссылку для помощи себе.
3. Вы отвечаете да указываете сумму возможной помощи как намерение и попадаете в сеть своего друга.
4. Вы приглашате знакомых помогать своему другу.

<b>Сценарий 3.</b> Ваш друг уже в сети Эксодус. 
1. Ваш друг присылает вам реферальную ссылку и объясняет как пользоваться ботом.
2. Вы отвечаете да, указываете сумму возможной помощи как намерение и попадаете в сеть своего друга.
3. Теперь вы можете как помогать другим участникам, так и запрашивать помощь себе, изменив статус на 🔆 или 🆘.
4. Вы можете приглашать в сеть своих друзей через реферальные ссылки помощи участникам своей сети.

Сеть строится по доверительным связям, формализуя существующие отношения в малых группах. Сеть расширяется при встрече локальных сетей. Чем большему числу участников помогаете вы, тем больше возможностей для взаимной поддержки.
""",
        "en":
"""
<b>How Do I get started in the bot and add members to my network?</b>

The growth of the network starts with who needs help.

<b>Scenario 1:</b> You need help. You are not on anyone's network yet.
1. You register in the bot using the start link https://t.me/exodus_commitbot. The default registration status is ✅.
2. Decide where the bot users can turn to contact you or get to know your situation better - it can be a social network, chat in a messenger, a website, etc. - any resource convenient for you.
3. Fill in your 👤Profile data:
✅Status - change status to 🔆 regular assistance or 🆘 emergency assistance, indicate the amount of the fee.
💬About me - you can enter brief information about yourself and a link to the discussion (optional, limited to 180 characters).
💳Details - you can set the details for providing financial assistance (bank card, payment system, link to the collection service, etc. By default, "" ask in person ").
4. Now you can in the main menu item 🔗Help create a referral link for help and send it to friends.
Friends who are ready to help you get into your network and can also use a bot for mutual assistance.

<b>Scenario 2.</b>
1. You want to organize a collection of help for a friend according to Exodus principles and are ready to help him. In this case, you yourself do not need help.
2. You explain to your friend what to do to start creating an autonomous reference network.
3. Your friend acts according to scenario 1, sends you a link to help himself, indicate the amount of possible help as an intention and get into your friend's network.
4. You can invite other friends you know to help your friend and help other members of this network.

<b>Scenario 3.</b>
1. Your friend sends you a referral link and explains how to use the bot.
2. You answer “yes”, indicate the amount of possible assistance as an intention and fall into your friend's network.
3. Now you can both help other participants and request help for yourself by changing the status to 🔆 or 🆘.
4. You can invite your friends to the network through referral links to help members of your network.  


The network is built on trust relationships, formalizing existing relationships in small groups. The network expands when local networks "meet". The more participants you help, the more opportunities for mutual support you got.
"""
    }

TEXT_CASE = \
    {
        "ru":
"""
<b>Возможные кейсы для использования бота Exodus</b>

<b>Обеспечение базового дохода иждивенцам:</b> дети, родители, инвалиды, заболевшие, семьи в тяжёлой жизненной ситуации, временно потерявшие работу и тп. Помощь нуждающимся оказывается адресно и непосредственно. Личное соучастие исключает сборы мошенниками. Распределенное внимание снижает нагрузку на каждого заботящегося. Система Эксодус стремится не держать человека в позиции только получающего, но помогает выйти из тяжёлой ситуации связями и компетенциями. Получатели регулярной помощи посильно участвуют во взаимном обмене.

<b>Касса взаимовыручки.</b> Страховая помощь среди круга договорившихся участников. Возможность быстрого оповещения и оказания помощи друг другу в ситуации временных затруднений среди круга друзей. 

<b>Базовый доход для творцов и деятелей немонетизируемых профессий.</b> В условиях кризиса многие творцы музыканты, художники, писатели оказались в ограниченных условиях . Платформы типа Патреона значительную часть передаваемых средств тратят на самообслуживание. Эксодус помогает сделать формат поддержки творцов их ценителями простым, прямым и прозрачным. Творец может свободно творить и не думать о хлебе насущном или путях продажи своего труда. 

<b>Представители некоммерческого сектора.</b> Сейчас деятельность многих НКО зависит от грантов, а это ограничение на использование средств, большой объем отчетности, отвлекающий от непосредственного оказания помощи. Эксодус может помочь с прямыми сборами среди физических лиц, чтобы снизить зависимость от грантов для обеспечения непрерывности своей работы. Может помочь со сборами для новых организаций или неформальных сообществ или направить поток помощи непосредственно к нуждающимся.

<b>Сбор на общие мероприятия.</b> Используя бот Эксодус, можно сделать прозрачным процесс сбора средств на общие мероприятия, будь это выезд на шашлыки, ежемесячная работа клуба по интересам, творческий фестиваль. Бот позволяет увидеть, что инициатива не собрала достаточного числа интересантов и отказаться от её реализации до того, как начать тратить реальные средства.

<b>Экстренные сборы.</b> Свадьба, похороны, покупка машины, строительство дома, обучение детей. Пожар, авария, лечение. Стартовый капитал. 
Иногда людям требуется собрать достаточно крупную сумму в ограниченное время. Эксодус позволяет оповестить друзей о такого рода нужде и получить разовую безвозмездную поддержку.

<b>Благотворители и меценаты</b>, используя бот Эксодус, получают возможность выбирать круги своей заботы, оказывать помощь тому, кто им более близок, находить единомышленников, оптимально распределять свои средства по большему кругу нуждающихся, сокращать издержки на посредников и непроизводительные траты. Решая этим задачи социального благополучия общества, от которого напрямую зависит их собственное.

<b>Учёт оказанных безвозмездных услуг.</b> Взаимная помощь может быть оказана и в немонетарной форме - консультация, массаж, урок, ремонт, транспортные услуги, предоставление помещения и тд. Все эти формы помощи можно перевести в денежный эквивалент и учесть как исполненное обязательство. Это помогает включить в продуктивные взаимодействия людей, у которых нет денежных средств. Помогает начать ценить "бесплатные" услуги. Это может стимулировать немонетарные обмены услугами, выводя людей из зоны вынужденной беспомощности от отсутствия денег.

Вы можете найти другие ситуации использования системы Эксодус и сообщить нам об успешных кейсах в обратной связи.
""",
        "en":
"""
<b>Possible Cases for Using the Exodus Bot</b>

<b>Providing basic income for dependents:</b> children, parents, disabled people, sick, families in difficult life situations, temporarily losing their jobs, etc. Help is provided to those in need directly and directly. Personal complicity excludes fraudulent fees. Distributed attention reduces the burden on each caregiver. The Exodus system seeks not to keep a person in the position of only receiving, but helps to get out of a difficult situation with connections and competencies. Recipients of regular assistance participate in mutual exchange as much as they can.

<b>Cashier of mutual assistance.</b> Insurance assistance among the circle of agreed participants. The ability to quickly alert and help each other in a situation of temporary difficulties among a circle of friends.

<b>Basic income for creators and non-monetized professions.</b> During the crisis, many creators, musicians, artists, writers found themselves in limited conditions. Platforms like Patreon spend a significant part of the transferred funds on self-service. Exodus helps make the support format for creators by their connoisseurs simple, direct and transparent. The creator can freely create and not think about his daily bread or ways to sell his labor.

<b>Representatives of the non-profit sector.</b> Now the activities of many NGOs depend on grants, and this is a restriction on the use of funds, a large amount of reporting, distracting from direct assistance. Exodus can help with direct collection to individuals to reduce reliance on grants for business continuity. Can help with fees for new organizations or informal communities.

<b>Gathering for general events.</b> Using the Exodus bot, you can make the process of collecting funds for general events transparent, be it going out to barbecue, the monthly work of a hobby club, or a creative festival. The bot allows you to see that the initiative has not collected a sufficient number of interested parties and to abandon its implementation before starting to spend real funds.

<b>Emergency fees.</b> Wedding, funeral, buying a car, building a house, teaching children. Fire, accident, treatment. Start-up capital.
Sometimes people need to raise a fairly large amount in a limited time. Exodus allows you to notify your friends about this kind of need and get one-time support for free.

<b>Benefactors and patrons</b>, using the Exodus bot, get the opportunity to choose the circles of their care, provide assistance to those who are closer to them, find like-minded people, optimally distribute their funds to a wider circle of those in need, reduce the costs of intermediaries and unproductive spending. Solving this problem of social well-being of society, on which their own directly depends.

<b>Accounting for rendered gratuitous services.</b> Mutual assistance can also be provided in a non-monetary form - consultation, massage, lesson, renovation, transport services, provision of premises, etc. All these forms of assistance can be converted into cash and recorded as a fulfilled obligation. It helps to include people who have no money in productive interactions. Helps to start appreciating "free" "services. This can stimulate non-monetary exchanges of services, taking people out of the zone of forced helplessness from lack of money

You can find other situations of using the Exodus system and inform us about successful cases in the feedback.
"""
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
