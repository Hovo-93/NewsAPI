# NewsApi Service
## Описание
Список технологий: Python, Django Rest Framework, Docker, Gunicorn, Nginx, PostgreSQL


#### Задача:
Необходимо создать сервер авторизации и новостей с комментариями и лайками на 

## Установка
#### Шаг 1. Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
bash
docker -v
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 2. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/NewsAPI.git
```
#### Шаг 3. Создайте в клонированной директории файл .env
Пример:
```bash
SECRET_KEY=django-insecure-7gek3pyo-)7@+^krv#-81l5-zx^^+d0t9daju_#z9%r=czjg%n
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=admin
DB_PASSWORD=admin1234
DB_HOST=db
DB_PORT=5432
```

#### Шаг 4. Запуск docker-compose
Для запуска необходимо выполнить из директории с проектом команду:
```bash
docker-compose up -d
```
#### Документация
Документация к API доступна по адресу:
json
http://localhost:8080/swagger/

##### Другие команды
Создание суперпользователя:
```bash
    docker-compose exec web python manage.py createsuperuser
```
Для пересборки и запуска контейнеров воспользуйтесь командой:
```bash
    docker-compose up -d --build 
```
Останавливаем и удаляем контейнеры, сети, тома и образы:
```bash
Stop and Delete containers

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

Delete Images
docker rmi $(docker images -a -q)
```
## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### Создание Юзера
```json
POST http://localhost:8000/api/v1/auth/users/
```
### Получаем Токен
```json
GET http://localhost:8000/auth/token/login/


# Body(json)
{
    "Username":"admin"
    "Password":"admin"
}
```

### Получаем список новостей с пагинацией
```json
GET http://localhost:8000/api/v1/news/
```
### Создаем новость
```json
POST http://127.0.0.1/api/v1/accrual/

# Body(json)
{
    "title": "lorem",
    "content": "lorem content"
}
```
### PUT news (обновляем новость, проерка на атворизацию, проверка на наличие прав)

json
POST http://todo

# Body(json)
{
    #todo
}
### DELETE news

json
POST http://127.0.0.1/todo

# Body(json)
{
    
}
### GET comments (получение списка комментариев новости с пагинацией)

json
GET http://127.0.0.1/todo

# Body(json)
{
    "id": 1
}
### POST comments (создание нового комментария, проверка на авторизацию)

json
GET http://127.0.0.1/todo

# Body(json)
{
    "id": 1
}

### DELETE comments 

### Like