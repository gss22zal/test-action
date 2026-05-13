# Flask Action Test Application

Простое Flask приложение для тестирования GitHub Actions.

## 🚀 Описание

Это тестовое приложение создано для демонстрации и отладки workflow GitHub Actions. Включает в себя:
- Базовое Flask приложение с API endpoint
- Docker конфигурацию для контейнеризации
- Готовые workflow для CI/CD тестирования

## 📦 Структура проекта

```
test-action/
├── .github/workflows/  # Конфигурации GitHub Actions
├── app.py              # Основное приложение
├── requirements.txt    # Зависимости Python
├── Dockerfile          # Конфигурация Docker образа
├── docker-compose.yml  # Docker Compose конфигурация
├── .dockerignore       # Исключения при сборке Docker
└── README.md           # Документация
```

## 🛠️ Требования

- Python 3.9+
- Docker (опционально, для контейнеризации)
- Docker Compose (опционально)

## 📥 Установка и запуск

### Локальный запуск

1. **Клонировать репозиторий:**
```bash
git clone <repository-url>
cd test-action
```

2. **Установить зависимости:**
```bash
pip install -r requirements.txt
```

3. **Запустить приложение:**
```bash
python app.py
```

Приложение запустится на `http://localhost:5000`

### Запуск через Docker

```bash
docker build -t test-action .
docker run -p 5000:5000 test-action
```

### Запуск через Docker Compose

```bash
docker-compose up --build
```

## 🌐 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/` | Главная страница |
| GET | `/health` | Проверка состояния приложения |
| GET | `/api/status` | Возвращает статус приложения в JSON |

## 🤖 GitHub Actions

### Доступные workflows

| Workflow | Описание | Триггер |
|----------|----------|---------|
| `ci.yml` | Сборка, тестирование и линтинг кода | Push, Pull Request |
| `docker.yml` | Сборка и публикация Docker образа | Push, Pull Request, Tags |
| `deploy.yml` | Деплой приложения в production | Push в main branch, Tags |

### Настройка secrets

Для работы деплоя необходимо настроить следующие секреты в репозитории:

| Secret | Описание |
|--------|----------|
| `SSH_HOST` | Хост сервера для деплоя |
| `SSH_USER` | Пользователь SSH |
| `SLACK_WEBHOOK` | Webhook для уведомлений (опционально) |

Управление секретами: **Settings → Secrets and variables → Actions → New repository secret**

## 🧪 Тестирование

Запуск тестов локально:
```bash
pytest
```

## 📝 Переменные окружения

| Переменная | Описание | Значение по умолчанию |
|------------|----------|----------------------|
| `FLASK_ENV` | Режим работы приложения | `development` |
| `PORT` | Порт для запуска | `5000` |

## 🔧 Конфигурация

Приложение конфигурируется через переменные окружения или файл `.env`:

```env
FLASK_ENV=production
PORT=5000
```

## 📄 License

MIT License

