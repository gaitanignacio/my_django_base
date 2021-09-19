# My Django Base

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/gaitanignacio/my_django_base.git
$ cd my_django_base
$
$ # Virtualenv installation
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application
$ python manage.py runserver
$
$ # Create superuser
$ python manage.py createsuperuser
$
$ # Add apps
$ python manage.py startapp app_name
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```