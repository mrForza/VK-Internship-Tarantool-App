## Структура проекта

<br>

**Общая структура проекта:**

``` bash
VK-Internship-Tarantool-App
|
├─── .gitignore <--- ?
|
├─── docker-compose.yml <--- Файл для запуска среды с несколькими контейнерами
|
├─── README.md <--- Главное описание проекта
|
├─── authorization_service <--- Микросервис авторизации пользователей в системе
|
├─── tarantool_infra <--- Директория с файлами для инициализации Tarantool-ов
|
├─── key_value_service <--- Микросервис обработки запросов на чтение-добавление пар ключ-значение
|
└─── documentation <--- Директория с описаниями проекта (структура, архитектура, user-guides, описание api)

```

<br>

**Cтруктура микросервиса авторизации:**
``` bash
C:.
|   .dockerignore
|   Dockerfile
|
├─── certificates
|       private_key.pem
|       public_key.pem
|
├─── src
|   |   config.py
|   |
|   |   main.py
|   |
|   |   poetry.lock
|   |
|   |   pyproject.toml
|   |
|   ├─── application
|   |    |
|   |    ├─── auth
|   |    |
|   |    └─── user
|   |
|   ├─── domain
|   |    |
|   |    ├─── common
|   |    |
|   |    ├─── entities
|   |    |
|   |    ├─── events
|   |    |
|   |    ├─── exceptions
|   |    |
|   |    └─── value_objects
|   |
|   ├─── infrastructure
|   |    |
|   |    └─── db
|   |         |
|   |         ├─── common
|   |         |
|   |         └─── repositories
|   |
|   └─── presentation
|        |
|        └─── api
|             |
|             ├─── controllers
|             |
|             └─── providers

```