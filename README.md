# Что выполнено
1) API из двух эндпоинтов
    - GET http://localhost:8000/battle/{id}
    - POST http://localhost:8000/battle/start
    Пример Json:
    ```
    {
        "fighter_1": {
            "name": "Воин",
            "power": 60
        },
        "fighter_2": {
            "name": "Рыцарь",
            "power": 50
        }
    }
    ```

Выйгравший определяется по его power и рандома, а именно power + randint(-20, 20) у кого больше тот победил

2) Docker
    - Есть Dockerfile для запуска приложения
    - docker-compose.yml для запуска всех контейнеров

Запуск докера (запускать в корневой папке):
```
docker compose build
docker compose up
```
Если хотите запустить через fastapi
```
cd src
fastapi dev main.py
```

## По коду
Слои:
- domain - есть только сущности
- application - бизнес-логика
- persistence - работа с бд (только redis)
- api

## Тесты
Сделал моки для Redis, чтобы не зависеть от него
test_get_battle:
- `test_get_battle_success` - проверка получения победителя
- `test_get_battle_not_found` - проверка возращения None если нет 
    правильней было бы так написать, так как NOT FOUND это именно ошибка 404:
    ```
    assert response.status_code == status.HTTP_404_NOT_FOUND
    ```
    но я хотел, чтобы тесты проходили


test_start_battle
- `test_start_battle_success` - успешный post запрос
- `test_start_battle_invalid_input` - не успешный, так как соответсвует модели