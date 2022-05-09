# misty_dc
Deploy ML with Django and Docker, I think it's kinda overkill, but a good learning project

1. create venv, pip install django
```
virtualenv env
env\Scripts\activate.bat
pip3 install django
```
2. Start project 
```
cd backend
django-admin startproject mysite
cd mysite folder
pip3 install djangrestframework
pip3 install markdown
pip3 install django-filter
```
3. python3 manage.py migrate
4. Start endpoints in the project 
```
python3 manage.py startapp endpoints
```
5. create apps, put appname in it 
6. change apps.py name to apps.endpoints

7. edit apps/endpoints/models.py
8. add apps/endpoints/serializers.py
9. edit apps/endpoints/views.py
10. add the links to urls 
11. edit settings
```
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'rest_framework',
      'apps.endpoints',
      'apps.ml'] 
  ROOT_URLCONF = 'misty_dc.urls'
```
12. edit asgi.py 
```
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misty_dc.settings')
```
13. edit urls.py
```
  from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns
  urlpatterns += endpoints_urlpatterns
```
14. Make registry to add connect the ML to server side (the worst nightmare)
15. use wsgi.py to add MLAlgorithm 
