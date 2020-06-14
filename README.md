# django-app
Writing My first Django app

If django was installed then check the version of the usind ```python -m django --version```

### Creating a project
```
django-admin startproject myApp
```
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
These files are:

- The outer myApp/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner myApp/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. myApp.urls).
- myApp/__init__.py: An empty file that tells Python that this directory should be considered a Python package. 
- myApp/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- myApp/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- myApp/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
***
### The development server

```
python manage.py runserver
```
***
### Creating the Polls app

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

To create your app, make sure you’re in the same directory as manage.py and type this command:

```
python manage.py startapp polls
```

That’ll create a directory polls, which is laid out like this:

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

***
### Write your first view

Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

 ```polls/views.py```
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

In the polls/urls.py file include the following code:

- polls/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:


- mysite/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

```
python manage.py runserver
```







