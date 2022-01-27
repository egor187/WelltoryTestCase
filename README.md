Тестовое задание Welltory на вакансию python-developer.

REST-API приложение, включающие 3 web-сервиса: генератор данных, импортер и обработчик

Стэк:
1. python 3.10
2. django 
3. drf
4. postgresql
5. celery
6. redis
7. faker
8. loguru

Установка:

1. git pull проект
2. docker-compose up -d --build
3. [curl, postman] -> 
    a) http://localhost:8000/run-import-task/ (основная таска оп импорту данных);
    b) http://localhost:8000/run-import-task/<int:pk> (доп таска: api для получения конкретного юзера)