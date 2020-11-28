# How to use this template

```
mkdir new-django-project && cd $_
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject \
--template https://github.com/conatussw/django-heroku-template/archive/main.zip \
--name=docker-compose.yml \
--name=Procfile \
new_django_project .
```
# Running the application using docker
`docker-compose up`

# In case of change something on docker files or add new dependencies to requirements.txt
`docker-compose up --build`

# Helpful commands
`docker-compose start|stop|restart`

# Direct access to containers
* docker-compose exec db sh
* docker-compose exec web sh
