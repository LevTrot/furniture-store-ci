# Furniture Store API

Backend-проект магазина мебели на Python, FastAPI, PostgreSQL и SQLAlchemy.

## Возможности

- CRUD для категорий
- CRUD для товаров
- CRUD для заказов
- PostgreSQL как основная база данных
- pytest-тесты
- coverage с порогом 50%
- линтер ruff
- Docker
- CI/CD через GitHub Actions

## Структура проекта

- `app/` — исходный код приложения
- `tests/` — тесты
- `.github/workflows/ci.yml` — CI/CD pipeline
- `Dockerfile` — сборка Docker-образа
- `docker-compose.yml` — запуск приложения и PostgreSQL
- `.env` — локальные переменные окружения

## Требования

- Docker
- Docker Compose
- Python 3.11
- PostgreSQL не нужно устанавливать вручную, при использовании Docker Compose

## Установка и запуск

### 1. Скопировать пример окружения
```bash
cp .env
```

### 2. Запустить приложение
```bash
docker compose up --build
```

#### После запуска API будет доступно по адресу: 
```bash
http://localhost:8000
```

### 3. Открыть документацию Swagger
```bash
http://localhost:8000/docs
```

#### Запуск тестов
```bash
docker compose exec app pytest
```

#### Запуск линтера
```bash
docker compose exec app ruff check .
```

## Описание API

### Categories
- POST /categories/
- GET /categories/
- PUT /categories/{category_id}
- DELETE /categories/{category_id}

### Products
- POST /products/
- GET /products/
- PUT /products/{product_id}
- DELETE /products/{product_id}

### Orders
- POST /orders/
- GET /orders/
- DELETE /orders/{order_id}

## Переменные окружения
### Содержимое .env (пример):    
POSTGRES_DB=furniture
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASE_URL=postgresql://postgres:postgres@db:5432/furniture

## CI/CD
При открытии pull request запускается pipeline, который:
1. проверяет сборку
2. запускает линтер
3. запускает тесты и coverage
4. собирает Docker-образ
5. отправляет образ в Docker Hub
