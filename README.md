# Django tutorial

# How to Deploy

### Droplets
- create ssh key for server (ssh-keygen -t rsa)
- add to Github (cat ~/.ssh/id_rsa.pub)
- git clone project into '/home/django'
- rename the default 'django_project' to 'django_project2'
- rename your project app to 'django_project'
- edit 'etc/systemd/system/gunicorn.service' (... **forward**.wsgi:application)
- edit 'etc/nginx/sites-enabled/default' (path)
- pip install -r requirements.txt
- eit forward/settings.py (ALLOWED_HOST=['*'])
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- systemctl daemon-reload
- systemctl restart gunicorn
- (restart droplet if changes not take effect)

### App
[reference](https://docs.digitalocean.com/tutorials/app-deploy-django-app/#step-4-deploying-to-digitalocean-with-app-platform)

![image](https://user-images.githubusercontent.com/51041738/184077759-7ddf4503-6a61-404b-bc6c-deb71d5c5740.png)

- Give access of repo to DigitalOcean

#### Build Command
- python manage.py makemigrations
- python manage.py migrate

#### Run Command
- gunicorn --worker-tmp-dir /dev/shm forward.wsgi

