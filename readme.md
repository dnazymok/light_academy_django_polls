# Django Pools App

> Light academy training project

### Installation
#### Docker

```
docker pull dnazymok/docker-lesson:latest
docker run -p 8000:8000 dnazymok/docker-lesson:latest
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