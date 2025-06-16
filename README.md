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
Сделал моки, чтобы не зависеть от БД
test_get_battle:
- `test_get_battle_success` - проверка получения по id
- `test_get_battle_not_found` - проверка возращения None если нет (должно быть 404, но я не сделал в api поэтому статус 200)

test_start_battle
- `test_start_battle_success` - начало битвы