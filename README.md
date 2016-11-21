# django-recetario
Examples and own notes about Django regarding this tutorial: http://www.maestrosdelweb.com/curso-django-instalacion-y-primera-aplicacion/

##Installing Django
I required to install Django 1.4.7, but I had troubles with it since when I created a Django project, it didn't create the manage.py file, which is necessary for starting the application. Instead, I took the version 1.4.12, and it fixed this problem.

##Initializing Django project with PyDev
Once I had PyDev plugin for Eclipse installed, I created a new Django Project by selecting "PyDev Django Project" on new project menu. I just clicked finish. (This step is the same as running "django-admin.py startproject recetario"
 on shell).
I had to add the path C:\Python27\Scripts on Python Interpreters. It's at Windows->preferences.

Finally, I ran the server by clicking on Run as -> PyDev: Django. (python manage.py runserver)

Next, I had to create the Django application, so I right clicked on the project folder -> Django -> create application, and I named it "principal". (python manage.py startapp principal)

We need to configure the settings.py file. We may configure these attributes:
- DATABASES
- ADMINS
- TIME_ZONE
- LANGUAGE_CODE
- INSTALLED_APPS: we have to add the app that we created when we runned the starapp command.
It's important to add #encoding:utf-8 at the beginning of the file.

Once we've configured the settings.py file, we have to run the following command in order to create the DB: python manage.py syncdb. It'll ask us for a superuser.

Now we've to modify the urls.py file in order to let us to acceed to the administrato's view. We'll add the following code:

```python
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
```
Now we can run the server, go to localhost:8000/admin and log in to the admin application.

