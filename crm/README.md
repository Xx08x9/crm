# crm — Задание 2: DRF, факультеты, направления, группы, API студентов

## Запуск
```bash
python -m venv venv
venv\Scripts\activate            # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Swagger: http://127.0.0.1:8000/api/docs/
- Админка: http://127.0.0.1:8000/admin/
- Вход для API (чтобы менять данные): http://127.0.0.1:8000/api-auth/login/

## Эндпоинты
| Метод | URL | Описание |
|---|---|---|
| GET/POST | /api/faculties/ | список / создание факультетов |
| GET/PUT/PATCH/DELETE | /api/faculties/{id}/ | один факультет |
| GET/POST | /api/directions/?faculty={id} | направления, фильтр по факультету |
| GET/POST | /api/groups/?direction={id} | группы, фильтр по направлению |
| GET/POST | /api/students/?group={id} | студенты, создание студента |

Читать могут все, изменять — только авторизованные (`IsAuthenticatedOrReadOnly`).
Пагинация — `PageNumberPagination`, по 10 записей (`?page=2`).

## Проверка в Swagger
1. Войти через `/api-auth/login/` под суперпользователем (сессия подхватится в Swagger)
   или нажать **Authorize** → basicAuth.
2. POST /api/faculties/ → `{"name": "Информационные технологии", "short_name": "ФИТ", "dean": "Иванов И.И."}`
3. POST /api/directions/ → `{"code": "09.02.07", "name": "Программирование", "faculty": 1, "duration": 4}`
4. POST /api/groups/ → `{"name": "ПО-1-24", "direction": 1, "admission_year": 2024, "is_active": true}`
5. POST /api/students/ → `{"username": "aibek", "password": "Strong-Pass-123", "first_name": "Айбек",
   "last_name": "Асанов", "student_id": "S-001", "group": 1}`
   — в ответе пароля нет; в админке видно, что он хранится как хеш `pbkdf2_sha256$...`.
