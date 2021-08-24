echo "Migrate"
python manage.py migrate
echo "Cache table"
python manage.py createcachetable
echo "Run server"
python manage.py runserver 0.0.0.0:8000