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

6) Микросервис авторизации доступен по адресу: 
    ```
    http://localhost:8080/
    ```
    Микросервис чтения-записи пар ключ-значени доступен по адресу:
    ```
    http://localhost:9080/
    ```

<br>

ВНИМАНИЕ: если вдруг у вас будут недоступны порты 8080 или 8090, то нужно будет:
- В фале docker-compose.yml поменять входные порты у authorization_service и key_value_service
- В файле config.py authorization_service и key_value_service поменять значение порта датакласса APIConfig
- Поменять константу EXTERNAL_API_HOST файла config.py key_value_service'а. Указать новый порт

<br>

### Как запустить тесты

1) Проверяем наличие в системе утилиты Postman

2) При отсутствии данной утилиты нужно установить ее себе, следуя инструкциям с официального сайта:
    ```
    https://learning.postman.com/docs/getting-started/installation/installation-and-updates/
    ```

3) Авторизуемся в приложении. Правый верхний угол, иконка пользователя

4) В левом верхнем углу нажимаем на:
    ```
    Settings --> File --> Import --> Выбираем коллекцию тестов VK Internship Integration Tests.postman_collection.json, которая находится в папке postman_tests
    ```

5) Нажимаем на коллекцию тестов и запускаем ее