# Django tutorial

# How to Deploy

### Droplets


### App

![image](https://user-images.githubusercontent.com/51041738/184070016-7662831e-e3a5-4143-9c2b-2cd8959d09d5.png)
#### Run Command
- gunicorn --worker-tmp-dir /dev/shm forward.wsgi
- python manage.py makemigrations
- python manage.py migrate
