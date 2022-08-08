# cat_or_bread_bot

Результат тестового задания №1

Папка bot_app: файлы, отвечающие за Telegram-бот. Не скрыла токен бота, чтобы вы могли его использовать самостоятельно (бот больше ни для чего не используется, в другом случае токен был бы скрыт). Для запуска бота на локальном сервере достаточно запустить файл bot.py. Тут же хранятся все необходимые конфигурации в файле config.py.

Папка api: файлы, отвечающие за API. 

Существует два эндпоинта:

- /api/get-last-message - нужен для получения последнего сообщения, отправленного ботом пользователю. На вход принимает user_id пользователя, возвращает текст сообщения.
- /api/send-message - нужен для отправки сообщения пользователя боту. На вход принимает api_id и api_hash пользователя, нужные для авторизации, а так же текст сообщения (message_text), возвращает статус (OK или Error). Не хватило времени реализовать до конца из-за проблем с подключением к БД.

Папка db: методы для работы с базой данных и сам файл БД (SQLite). В репозиторий добавлен файл с данными для примера, можно заменить на пустой с аналогичным названием.

Схема БД:
![diagram (4)](https://user-images.githubusercontent.com/47586933/183430454-52186baa-ed51-46c8-812d-4fc07b39aaf0.png)
