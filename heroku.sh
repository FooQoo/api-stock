heroku run sh -c 'python manage.py migrate'
heroku run sh -c 'python manage.py createsuperuser'
heroku run sh -c 'python manage.py collectstatic'