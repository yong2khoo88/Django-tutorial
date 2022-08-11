# Django tutorial

# How to Deploy

### Droplets


### App
[reference](https://docs.digitalocean.com/tutorials/app-deploy-django-app/#step-4-deploying-to-digitalocean-with-app-platform)

![image](https://user-images.githubusercontent.com/51041738/184077759-7ddf4503-6a61-404b-bc6c-deb71d5c5740.png)

#### Build Command
- python manage.py makemigrations
- python manage.py migrate

#### Run Command
- gunicorn --worker-tmp-dir /dev/shm forward.wsgi

