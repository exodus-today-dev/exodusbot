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
GLOBE = '\U0001F310'  # Globe with Meridians
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
О чем вы хотите узнать?",
        "en":
            "Bot Exodus - \n\
organization of decentralized network mutual assistance.\n\n\
What do you want to know?"
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
            f"*Условные обозначения в боте:*\n\n" \
            f"*Статус пользователя:*\n" \
            f"{GREEN_BALL} - готов помогать участникам сети, сейчас помощь не требуется;\n" \
            f"{ORANGE_BALL} - необходима ежемесячная поддержка для обеспечения базовых нужд, могу помогать другим участникам сети;\n" \
            f"{RED_BALL} - требуется экстренная помощь в ограниченный срок, закрывается только обязательствами.\n\n" \
            f"*Финансовые показатели:*\n" \
            f"Расчетная единица в текущей версии бота - USD\n" \
            f"{MONEY_BAG} - объем ежемесячной или экстренной помощи, задаётся в профиле при смене статуса, может корректироваться в профиле;\n" \
            f"{HEART_RED} - объем намерений, может быть скорректирован или свободно отозван, показывает " \
            f"готовность участников сети соучаствовать в помощи, переводится в обязательства;\n" \
            f"{HANDSHAKE} - обязательства, договоренность помочь, могут храниться или предъявляться к исполнению, обязательство нельзя отозвать;\n" \
            f"{LIKE} - исполненное обязательство, исполнение обязательства подтверждается получателем помощи;\n" \
            f"{HELP} - объем помощи, не закрытой обязательствами, уменьшается по мере перевода намерений в обязательства и их исполнения.\n\n" \
            f"*Как прочитать данные о пользователе:*\n" \
            f"User Lastname {ORANGE_BALL} / {GLOBE} Позвать / {SPEECH_BALOON} www.mypage.info / {CREDIT_CARD} PayPal User.blabla@gmail.com\n" \
            f"2 {PEOPLES}{RIGHT_ARROW}{MAN} (75.0 {HEART_RED} / 475.0 {HELP})\n" \
            f"{MAN} -> 2 {PEOPLES} (20.0 {HEART_RED} / 10.0 {HANDSHAKE})\n" \
            f"User Lastname в оранжевом статусе, может помогать и принимать помощь. Чтобы помочь ему, нужно кликнуть на ссылку {GLOBE} Позвать или скопировать её и послать друзьям.\n" \
            f"Узнать подробнее о ситуации пользователя и его сбора можно по ссылке 💬www.mypage.info.\nУказаны реквизиты для помощи.\n\n" \
            f"Два участника сети помогают этому пользователю сейчас, объем их намерений равен 75 и это меньше требуемой для закрытия сбора суммы в 475 USD." \
            f"Этот пользователь сейчас помогает двум участникам сети, его намерения равны 20, а взятые обязательства - 10 USD.",
        "en":
            "In procesing..."
    }
TEXT_MENU = \
    {
        "ru":
            f"*Главное меню бота Эксодус*\n\n" \
            f"{MAN}*Профиль*\n" \
            f"* Статус* - указать актуальный статус и данные для помощи - сумму сбора и срок для экстренного сбора\n" \
            f"* {SPEECH_BALOON}Изменить* - задать ссылку для обсуждения обстоятельств сбора (по умолчанию - спросить лично)\n" \
            f"* {CREDIT_CARD}Реквизиты* - задать реквизиты для оказания помощи (по умолчанию - спросить лично)\n" \
            f"* {FOOTPRINTS}Выйти из бота* - удалиться из бота\n\n" \
            f"*{PEOPLES} Участники*\n" \
            f"* Моя сеть* {PEOPLES} 3 - количество и список всех участников референтной сети и ситуация их сбора:\n" \
            f"       ID1 Name1 {GREEN_BALL}" \
            f"       ID2 Name2 {ORANGE_BALL} 50{HEART_RED}/500{HELP}🏻 (в пользу участника 50 намерений, объем требуемого и незакрытого обязательствами сбора 500)\n" \
            f"       ID3 Name3 {RED_BALL}  500{HELP} / 10 дней (в течение десяти дней участнику требуется набрать 500 USD)\n\n" \
            f"       При указании ID участника можно увидеть:\n" \
            f"       *Данные профиля User*, включая ссылку на обсуждение его ситуации,  реквизиты для помощи, ссылку для оказания помощи\n" \
            f"       *Сеть {PEOPLES} User* - список всех, включенных в референтную сеть этого пользователя\n" \
            f"       *User{RIGHT_ARROW}{PEOPLES}* - список тех, кому этот пользователь уже помогает\n" \
            f"       *{PEOPLES}{RIGHT_ARROW}User* - список всех, кто помогает этому пользователю. " \
            f"Если вы тоже ему помогаете, то увидите всю ситуацию по сбору, если еще не помогаете - то доступен " \
            f"только общий список помогающих\n" \
            f"       *Помочь User* - реферальная ссылка для помощи этому пользователю бота, " \
            f"которую можно разослать друзьям. При клике на ссылку происходит переход в бота и " \
            f"появляется запрос о возможности помощи выбранному пользователю.\n\n" \
            f"*Расширить сеть* - производит автоматическое расширение вашей референтной сети после " \
            f"включения в вашу сеть новых участников, в отношении которых вы проявляете намерения помочь. " \
            f"Вы начинаете видеть других участников сети, которые также помогают выбранному вами пользователю.\n\n" \
            f"🗓*Органайзер* - управление намерениями и обязательствами:\n" \
            f"*3{HEART_RED}/ 1🤝 -> {MAN}* - показывает число актуальных намерений и обязательств в мою пользу, " \
            f"позволяет формировать запросы на перевод {HEART_RED} в 🤝 и исполнение сохраненных ранее обязательств\n" \
            f"*{MAN}->2{HEART_RED} / 2🤝* - показывает число актуальных намерений и обязательств в пользу " \
            f"других участников сети, позволяет управлять ими: для намерений{HEART_RED} -  отзывать, " \
            f"корректировать сумму, переводить в обязательства; " \
            f"для обязательств 🤝 - подтвердить исполнение, напомнить позже.\n" \
            f"*3/450{LIKE} ->{MAN}->2/240{LIKE}* - архив исполненных обязательств в мою пользу и моих " \
            f"в пользу других участников сети (общее число/сумма осуществленных переводов в отчетный период)\n\n" \
            f"*{MAN}-> 3 {PEOPLES}* Список всех, кому я помогаю в текущий период и чем именно, с возможностью просмотреть их данные по ID\n" \
            f"*2 {PEOPLES}{RIGHT_ARROW}{MAN}* Список всех, кто помогает мне в текущий период, с возможностью просмотреть их данные по ID\n\n" \
            f"*🤝->{LIKE} 2->{MAN}->2* список всех обязательств, которые отправителем отмечены как исполненные, " \
            f"а получателем еще не подтверждены. Дают возможность отметить исполнение обязательства в свою пользу " \
            f"и направить уведомление-напоминание с просьбой подтвердить исполнение.\n\n" \
            f"*{QUESTION}FAQ* - описывает основные возможности работы бота\n\n" \
            f"*{SPEECH_BALOON}Help* - ссылка на канал с подробными инструкциями и объяснениями работы системы Эксодус. " \
            f"Возможность задать вопрос в техподдержку, если что-то в работе бота не ясно, сообщить об ошибках, " \
            f"высказать свои замечания и предложения о дальнейшем совершенствовании бота.\n\n" \
            f"*{GLOBE}Позвать* - показывает список всех участников референтной сети, у которых сейчас идет активный сбор, " \
            f"с формированием реферальной ссылки для помощи каждому из них.",
        "en":
            "In procesing..."
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

TEXT_SUM_DIGIT = {'ru': 'Сумма должна быть только в виде цифр.',
                  'en': 'The amount should only be in the form of numbers.'}

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
    lang = read_user_language(message.chat.id).language
    if lang == "ru":
        msg = "Пошло что-то не так. Попробуйте снова!"
    else:
        msg = "Something went wrong. Try again!"
    return msg
