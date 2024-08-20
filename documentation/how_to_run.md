### Как запустить приложение

1) Клонируем репозиторий через http или ssh
    ``` bash
    git clone git@github.com:mrForza/VK-Internship-Tarantool-App.git
    ```

2) Переходим в корневую директорию проекта
    ``` bash
    cd VK-Internship-Tarantool-App
    ```

3) Проверяем наличие на устройстве утилиты docker-compose
    ``` bash
    docker-compose --version
    ```

4) Собираем проект
    ``` bash
    docker compose build
    ```

5) Запускаем проект
    ``` bash
    docker compose up -d
    ```

6) Микросервис авторизации доступен по адресу: http://localhost:8080/

    Микросервис чтения-записи пар ключ-значени доступен по адресу: http://localhost:9080/