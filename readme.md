# Django Pools App

> Light academy training project

### Installation
#### Docker

```
git clone --branch docker-lesson https://github.com/dnazymok/light_academy_django_polls.git
cd light_academy_django_polls
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createcachetable
```

#### or

```
git clone https://github.com/dnazymok/light_academy_django_polls.git
cd light_academy_django_polls
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createcachetable 
python manage.py runserver
```