# misty_dc
Deploy ML with Django and Docker 

1. create venv, pip install django
 virtualenv env
env\Scripts\activate.bat
pip3 install django
cd backend
2. django-admin startproject mysite
3. cd mysite folder
4. python3 manage.py migrate
pip3 install djangrestframework
pip3 install markdown
pip3 install django-filter
5. python3 manage.py startapp appname (endpts)
6. create apps, put appname in it 
7. change apps.py name to apps.appname
8. models.py (class charfield)
9. settings.py (add)
rest_framewk, apps.endpt, apps.ml
10. edit apps/endpoints/models.py
11. add apps/endpoints/serializers.py
12. edit apps/endpoints/views.py
13. add the links to urls 
14. edit settings
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
16.edit asgi.py 
```
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misty_dc.settings')
```
17. edit urls.py
```
  from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns
  urlpatterns += endpoints_urlpatterns
```
19. use wsgi.py to add MLAlgorithm 
