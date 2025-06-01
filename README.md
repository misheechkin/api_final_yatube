# Yatube Social Network API v2.0

**RESTful API для социальной платформы блоггинга**
_Усовершенствованная версия с расширенными возможностями взаимодействия_

---

## 🛠 Технологический стек

| Категория       | Компоненты                                                                 |
|-----------------|----------------------------------------------------------------------------|
| **Ядро**        | Python 3.11 • Django 4.2                                                   |
| **API**         | DRF 3.14 • SimpleJWT 5.2                                                   |
| **База данных** | PostgreSQL 14 (рекомендуется) • SQLite3 (для разработки)                   |
| **Деплой**      | Gunicorn • Nginx • Docker                                                  |
| **Дополнения**  | pytest • Celery • Redis                                                    |

---

## 🚀 Быстрый старт

### Требования среды
- Интерпретатор Python ≥3.9
- Система управления пакетами pip
- Виртуальное окружение (рекомендуется)

### Инициализация проекта
```bash
# Клонирование репозитория
git clone https://<repository_url> && cd yatube_api

# Инициализация виртуального окружения
python -m venv .venv && source .venv/bin/activate

# Установка зависимостей
pip install --upgrade pip && pip install -r requirements/dev.txt

# Миграции:
python3 manage.py migrate

# Запуск:
python3 manage.py runserver
```
