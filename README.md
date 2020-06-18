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

## Templates

Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. For a hands-on example of creating HTML pages with templates,

## Configuration

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
```
- settings:

- DIRS defines a list of directories where the engine should look for template source files, in search order.

- APP_DIRS tells whether the engine should look for templates inside installed applications. Each backend defines a conventional name for the subdirectory inside applications where its templates should be stored.

```
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
```

## Managing static files (e.g. images, JavaScript, CSS)

Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides django.contrib.staticfiles to help you manage them.

## Configuring static files

- Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.

- In your settings file, define STATIC_URL, for example:

```
STATIC_URL = '/static/'
```

- In your templates, use the static template tag to build the URL for the given relative path using the configured STATICFILES_STORAGE.

```
{% load static %}

<img src="{% static "my_app/example.jpg" %}" alt="My image">
```
- Store your static files in a folder called static in your app. For example my_app/static/my_app/example.jpg.

Your project will probably also have static assets that aren’t tied to a particular app. In addition to using a static/ directory inside your apps, you can define a list of directories (STATICFILES_DIRS) in your settings file where Django will also look for static files. For example:

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
```

python ./manage.py migrate
python ./manage.py makemigrations




