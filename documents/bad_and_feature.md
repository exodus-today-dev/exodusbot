## Недостатки текущей реализации системы и возможности их преодоления. 
1. Главный недостаток - это библиотека telebot, которая была использована для написания данного бота.
- Решением является использование aiogram. 

2. Для переходов между меню используются кнопки-клавиатуры и метод register_next_step_handler. 
Внутри этой связки переходов между меню не работают команда /start. 
Также для переходов между меню в коде были созданы глобальные словари для запоминания id пользователей и соответствующие им данные для сохранения. В результате, в случае перезапуска бота все эти данные удаляются.

3. В проекте предусмотрен модуль events_worker, который в бесконечном цикле опрашивает таблицу events в базе данных и при наличиии определенных неотправленных уведомлений происходит их обработка.
Это не является оптимальным, так как получается избыточность в базе за счет создания, контроля за исполнением этих событий.
- Вероятное решение - использовать паттерн наблюдатель или же осуществлять рассылку уведомлений на лету.

## Функции, которые были бы желаемы, но не реализованы в текущем боте: 
4. 
- мультиязычность и легкое добавление нового языка
- управление уведомлениями - выбор для пользователя, какие уведомления о событиях в своём круге он хотел бы видеть, а какие для него избыточные
- работа пользователей с разными валютами, сейчас условная валюта евро. Пользователи бота из разных стран и им было бы удобно видеть все расчеты в удобной форме. При этом сквозная логика суммирования намерений и обязательств требует единого формата. При этом, поскольку все реальные расчеты происходят за пределами бота, нет требований к доскональной точности. Хотелось бы избежать привязки к колебаниям курса.
- Возможность клиринга обязательств в круге - вычисление замкнутых циклов и раз в месяц взаимозачет хранящихся обязательств между участниками. 

5. Избыточное число кликов - нужна оптимизация интерфейса пользователя.

6. Рейтинг и карма пользователя - по ответственному исполнению взятых на себя обязательств. 

7. Возможность центрирования кругов вокруг пользователей - ближний круг, средний круг, дальний круг и приглашение к помощи по принципу концентрических окружностей - если не смогли закрыть потребность в ближнем круге - подключать более дальние.  

8. Сейчас бот работает на выявление децентрализованной сети взаимной помощи. В нем ещё не реализованы полноценно функции страховой кассы и совместного децентрализованного проектирования.

---
[Главная](index.md)
