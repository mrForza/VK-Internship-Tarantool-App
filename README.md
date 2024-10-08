## VK-Internship-Tarantool-App

<br>

VK-Internship-Tarantool-App - это микросервисное приложение, написанное на языке программирования Python, которое представляет из себя API к key-value хранилищу Tarantool

**Стэк технологий**: Python, FastAPI, Asynctnt, Tarantool, Git, Docker, Docker-compose, Lua, Postman

<br>

### Оглавление

- [Как запустить проект и тесты](documentation/how_to_run.md)

- [Документация API микросервисов](documentation/api_docs.md)

- [Структура приложения](documentation/structure.md)


<br>

### Функционал приложения

Приложение состоит из двух микросервисов: authorization_service и key_value_service. Взаимодействовать с ними можно по http протоколу (подразумевается использование Postman или любой другой утилиты).

Используемые архитектурные паттерны: Чистая архитектура, Domain-Driven-Design, CQRS, Репозиторий

<br>

**Функции Микросервиса авторизации:**

- **Регистрация новых пользователей**. Пользователь должен ввести логин, пароль, имя и фамилию.

    Некоторые ограничения на ввод данных:
    
    - Логин должен иметь размер 2 - 64 символа и состоять только из строчных-заглавных латинских букв и цифр

    - Пароль должен иметь размер 8 - 64 символа и иметь хотя бы одну строчную, заглавную латинскую букву, цифру и спец. символ

    - Логин должен иметь размер 2 - 32 символа и состоять только из строчных-заглавных латинских букв + знак "-"

    - Логин должен иметь размер 2 - 32 символа и состоять только из строчных-заглавных латинских букв + знак "-" 

    После того, как сервис провалидировал входные данные, он проверяет наличие в бд пользователя с таким же логином. Если такой пользователь уже есть, то приложение предлагает зарегистрироваться заново. При успешной регистрации все данные сохраняются в бд (пароль при этом хэшируется).
    
<br>

- **Аутентификация пользователя.** Пользователь должен ввести логин и пароль. Если в бд нет записи с таким логином, или введенный человеком пароль (после хэширования) не совпадает с тем паролем, который хранится в бд, то ему выдается сообщение об ошибке.

    При успешной аутентификации пользователю возвращается JWT токен, который он сам должен ввести в заголовки запроса. *Request headers --> Authorization: Bearer [token]*.

    Время жизни каждого токена - 30 минут. Далее токен становится невалидным.

<br>

- **Выход из аккаунта.** Пользователь может осуществить выход из аккаунта только в том случае, если в его заголовках запроса присутствует валидный JWT токен. В противном случае приложение сообщит ему о том, что он не аутентифицировался.

    При осуществлении выхода из аккаунта предполагается, что пользователь добровольно удаит из своих заголовков запроса данный JWT токен. В случае запуска тестов в утилите Postman заранее предусмотрено автоматическое удаление токена после выхода из аккаунта

<br>

<br>

**Функции Микросервиса авторизации:**

- **Чтение key-valye пар пачками.** Пользователь должен ввести список ключей, значение которых он хочет получить.

    Приложение может вернуть сообщение об ошибке, если:
    - Отсутствуют какие-либо ключи
    - Ключи повторяются
    - Некоторые ключи отсутствуют в бд

    В остальных случаях приложение асинхронно прочитает все key-value пары из бд и выведет их.

<br>

- **Запись пар key-value пачками.** Пользователь должен ввести множество key-value пар.

    Ограничения на ввод данных:
    - Хотябы одна key-value пара должна присутствовать
    - Не должно быть повторяющихся ключей
    - Ключи должны иметь тип *string* (json ограничение)
    - Value могут иметь любой тип и любую вложенность

    Если пользователь ввел пары key-value, которые уже присутствуют в бд, то программа предупреждает пользователя о том, что их добавление будет проигнорированно. Остальные валидные пары key-value записываются в бд в асинхронном режиме.