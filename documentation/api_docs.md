## Документация API микросервисов

### Эндпоинты *Микросервиса авторизации*:

- [Регистрация нового пользователя](http://localhost:8080/api/register/)

- [Аутентификация](http://localhost:8080/api/login/)

- [Выход из аккаунта](http://localhost:8080/api/logout/)

- [Получение всех пользователей](http://localhost:8080/api/users/)

- [Получение пользователя по логину](http://localhost:8080/api/users/{user_login}/)

- [Получить информацию про свой профиль](http://localhost:8080/api/users/me/)

<br>

### Эндпоинты *Микросервиса обработки пар key-value*:

- [Считать пары key-value](http://localhost:8090/api/read/)

- [Записать пары key-value](http://localhost:8090/api/write/)


<br>


### Описание эндпоинтов *Микросервиса авторизации*:

- **Регистрация нового пользователя**

    Путь: http://localhost:8080/api/register/

    Метод: POST

    Обязательная авторизация: НЕТ

    Возможные статус-коды:
    
    - 201 Пользователь успешно зарегистрировался
    - 400 Ошибка валидации: (некорректный логин/пароль/имя/фамилия или пользователь с таким логином уже существует)
    - 405 Некорректный метод запроса
    - 422 Некорректная структура запроса

    Пример успешного запроса: 
    ```
    {
        "login": "CorrectLogin123",
        "password": "Correct_Passw00rd123(&)^(",
        "name": "Roman",
        "surname": "Gromov"
    }
    ```
    Пример ответа на успешный запрос: 201
    ```
    {
        "message": "You have been successfully registered!"
    }
    ```
    Пример ответа, когда пользователь с таким логином уже был зарегистрирован: 400
    ```
    {
        "message": "A user with this login is already exists"
    }
    ```

<br>

- **Аутентификация в системе**

    Путь: http://localhost:8080/api/login/

    Метод: POST

    Обязательная авторизация: НЕТ

    Возможные статус-коды:
    
    - 201 Пользователь успешно аутентифицировался
    - 404 Ошибка: (нет пользователя с таким логином или неверный пароль)
    - 405 Некорректный метод запроса
    - 422 Некорректная структура запроса

    Пример успешного запроса: 
    ```
    {
        "login": "CorrectLogin123",
        "password": "Correct_Passw00rd123(&)^("
    }
    ```
    Пример ответа на успешный запрос: 201
    ```
    {
        "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSb21hbiBHcm9tb3YiLCJ1c2VybmFtZSI6IkNvcnJlY3RMb2dpbjEyMyIsImVtYWlsIjoiQ29ycmVjdExvZ2luMTIzIiwiZXhwIjoxNzI0MTYwNjE4LCJpYXQiOjE3MjQxNTg4MTh9.OLxdh7KG-LFo15WOlggogsPqaxJR665Ruji-NtnKcvn2HZ7MlKk7-1uEsNSBTaehMj7jWExGCFdYsvDWSB6aG2T28Ov8XliDaO-11YG2JLTKlkI1zFGP2vdvvQAPM_VGV4EA_VRMdeZFmZk_FvO2ZN6_1Pa8RcI7SuRt9pfYl_Ot0RVP5bjTROQ0HUS6SIZLtww43vNoPzPBHp1z7BiyPWW5QYjHv0ShFUvrSwbnlxhjz3UMow7Ex325M4r4kU7v4eSoZPqTr8pipEmvE9zAnXMms_HX7DD4zVcZYY3LNI9NTwsBAOsRhYJRqYDkZpqOWUJjKJD408VFB2jthK-f-A",
        "message": "You have been successfully authenticated"
    }
    ```
    Пример ответа, когда логин или пароль не совпадает: 404
    ```
    {
        "token": "-",
        "message": "You have entered an incorrect login or password"
    }
    ```

<br>

- **Выход из аккаунта**

    Путь: http://localhost:8080/api/logout/

    Метод: GET

    Обязательная авторизация: ДА

    Возможные статус-коды:
    
    - 200 Пользователь успешно вышел из аккаунта
    - 401 Ошибка авторизации: (отсутствует jwt токен, токен невалидный или он просрочился)
    - 405 Некорректный метод запроса
    - 422 Некорректная структура запроса

    Пример успешного запроса: 
    ```
    Request Headers:
        .
        Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSb21hbiBHcm9tb3YiLCJ1c2VybmF...
        .
    Тела у запроса НЕТ!!!
    ```
    Пример ответа на успешный запрос: 200
    ```
    {
        "message": "You have been successfully logout from your account! Please, remove a jwt token from your Authorization Headers) I'm so lazy to do it)"
    }
    ```
    Пример ответа, когда передается некорректный токен: 401
    ```
    {
        "message": "You have not been authorized!"
    }
    ```

<br>

### Описание эндпоинтов *Микросервиса обработки пар key-value*:

- **Чтение пар key-value**

    Путь: http://localhost:8080/api/read/

    Метод: POST

    Обязательная авторизация: ДА

    Возможные статус-коды:
    
    - 200 Пользователь успешно считал пары key-value
    - 400 Ошибка валидации: (отсутствуют ключи, имеются повторяющиеся ключи, ключи имеют некорректный тип)
    - 401 Ошибка авторизации: (отсутствует jwt токен, токен невалидный или он просрочился)
    - 405 Некорректный метод запроса
    - 422 Некорректная структура запроса

    Пример успешного запроса: 
    ```
    {
        "login": "CorrectLogin123",
        "password": "Correct_Passw00rd123(&)^(",
        "name": "Roman",
        "surname": "Gromov"
    }
    ```
    Пример ответа на успешный запрос: 200
    ```
    {
        "data": {
            "Key - Value (int)": 1,
            "Key - Value (string)": "Lorem ipsum doler sit amet",
            "Key - Value (float)": 3.14,
            "Key - Value (list)": [
                "a",
                "b",
                "c"
            ],
            "Key - Value (dict)": {
                "1": 1111111,
                "2": 2222222,
                "0": 0
            },
            "Key - Value (large nesting)": [
                {
                    "a": {
                        "a2": [
                            1,
                            2,
                            3
                        ]
                    },
                    "b": [
                        1,
                        2,
                        {
                            "q": "w",
                            "e": "r"
                        }
                    ]
                },
                {
                    "1": [
                        1,
                        2,
                        3
                    ],
                    "2": [
                        4,
                        5,
                        6
                    ]
                },
                {
                    "3": {
                        "3.2": 3.2,
                        "3.3.": 3.3
                    }
                }
            ]
        }
    }
    ```
    Пример запроса с повторяющимися ключами:
    ```
    {
        "keys": ["key1", "key2", "key1", "key1", "key2", "key5"]
    }
    ```
    Пример ответа, когда были переданы повторяющиеся ключи: 400
    ```
    {
        "message": "Incorrect keys: you cannot pass identical keys: key1 key2"
    }
    ```
    Пример ответа, когда пользователь не был авторизован: 401
    ```
    {
        "message": "You are not authorized! Please, sign in or sign up"
    }
    ```

<br>

- **Запись пар key-value**

    Путь: http://localhost:8080/api/write/

    Метод: POST

    Обязательная авторизация: ДА

    Возможные статус-коды:
    
    - 201 Пользователь успешно записал пары key-value
    - 400 Ошибка валидации: (отсутствуют пары key-value, повторяющиеся ключи)
    - 401 Ошибка авторизации: (отсутствует jwt токен, токен невалидный или он просрочился)
    - 405 Некорректный метод запроса
    - 422 Некорректная структура запроса

    Пример успешного запроса: 
    ```
    {
        "data": {
            "alphabet": [
                "a",
                "b",
            ],
            "numbers_and_hexes": {
                "123": "7B",
                "786487654": "2EE0D966"
            },
            "nested_key": {
                "a": {
                    "1": [
                        {
                            "a": "b"
                        }
                    ],
                    "2": {
                    "1": "2"  
                    },
                    "3": 1.123495
                },
                "b": {
                    "lorem": "ipsum"
                }
            }
        }
    }
    ```
    Пример ответа на успешный запрос: 201
    ```
    {
        "status": "success"
    }
    ```
    Пример ответа на повторный запрос на добавление данных: 201 (WARNING)
    ```
    {
        "status": "success, but these keys have not been written: alphabet numbers_and_hexes nested_key. Because they have already been in kv store"
    }
    ```
    Пример ответа, когда пользователь не был авторизован: 401
    ```
    {
        "message": "You are not authorized! Please, sign in or sign up"
    }
    ```

<br>