# misty_dc
Deploy ML with Django and Docker, I think it's kinda overkill, but a good learning project
This is a more fancy setup, if you just deploy one model (not gonna do anything about, refer to misty_dc_light)

1. Create venv and install Django
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
4. Start endpoints in the project 
```
python3 manage.py startapp endpoints
```
5. Create apps, put appname in it 
6. Change apps.py such that it knows we have moved the endpoints directory into apps
```
class EndpointsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.endpoints'
```
7. Edit apps/endpoints/models.py
8. Good time to migrate the fields into the db. 
```
python3 manage.py makemigrations
python3 manage.py migrate
```
10. Add apps/endpoints/serializers.py
11. Edit apps/endpoints/views.py
12. Add the links to urls 
13. Edit settings
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
  SECRET_KEY = 'django-insecure-' # delete just for security reason
```
12. Edit asgi.py 
```
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misty_dc.settings')
```
13. Edit urls.py
```
  from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns
  urlpatterns += endpoints_urlpatterns
```
14. Make registry to add connect the ML to server side (the worst nightmare)
15. use wsgi.py to add MLAlgorithm 
