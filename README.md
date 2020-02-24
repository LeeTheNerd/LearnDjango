# Django Core Fundamentals

This guide will cover the core fundamentals of the Django framework. This is meant to be used as a reference. There is no specific project associated with this guide and can be used along with any project.

## Prerequisite

- You are familiar with Python
- You understand virtual environments

## What is Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Some benefits of Django are

- Ridiculously Fast
  - Django was designed to help developers take applications from concept to completion as quickly as possible.
- Reliable Security
  - Django takes security seriously and helps developers avoid many common security mistakes.
- Exceedingly Scalable.
  - Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

[read more here](https://www.djangoproject.com/start/overview/)

---

## Install Django

- _Note: It is best to build apps in a virtual environment_

Django is installed using `pip`. To install Django run the following command using `pip` or `pip3`.

`pip install django`

This will install the following packages:

```
asgiref==3.2.3
Django==3.0.3
pytz==2019.3
sqlparse==0.3.0
```

- _Note: It is best to build apps in a virtual environment_

Python is now setup to use the Django framework.

---

## Start A Django Project

_from Django's official documentation_

A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

### _layman's terms_

All Django projects begin with a project. The project is the root folder for everything associated with the project including apps. Django will create this folder with the name specified in the `django-admin` command.

In the code example below. The project is called 'BlogSite'

`django-admin startproject WebProject`

This will create the following project in the file system as the root directory.

```
WebProject
 ┣ WebProject
 ┃ ┣ __pycache__
 ┃ ┃ ┣ settings.cpython-38.pyc
 ┃ ┃ ┗ __init__.cpython-38.pyc
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┗ manage.py
```

**Make sure you navigate into this directory**

Think of this directory as the server. You can run this server but there is no content associated with it. However, this is now a fully functional web server that can be started from the `manage.py` file. The files in the `WebProject` directory are all associated with integrating with the apps created and will be discussed later.

### The `manage.py` File

The `manage.py` file is command-line utility that lets you interact with this Django project in various ways.

## Start The Server

---

To start the server, run the following command. Since there is no app/website associated with this project yet, it will generated a generic Django landing page.

- _Note: Make sure you are in the directory of the file you are running_

`python manage.py runserver`

Once the server is started, the following information will be shown in the command line. Navigate to the local URL to see Django running.

```Django version 3.0.3, using settings 'BlogSite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

_There will be other output on the command line in regards to warnings and migrations. This can be ignored and will be covered later._

---

## Create an App

### What is an App

_from Django's official documentation_

An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app

### _layman's terms_

Think of an app as the website being hosted on the server. One app can be the entire website - e.g., a static 1 page site. Apps can also be components that combine with other apps within a project that create an entire website - e.g., main site, ecommerce page, users, etc.

The command to create an app is utilized with the `manage.py` file. There are 2 arguments needed after `python manage.py arg1 arg2`. The first argument tells Django to create a new application. That command is called `startapp` The second argument is what the application will be called. Its best to name the app something associated with its use.

Example:

```
python manage.py startapp BlogSite
```

This will generate the default Django files in a directory named after this application and will look like this:

```
BlogSite
 ┣ migrations
 ┃ ┗ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ tests.py
 ┣ views.py
 ┗ __init__.py
```

<br>

# Django's Default Files

All of the files in a Django project can interact with one another. There can also be a lot of confusion since Django creates a lot of files that are named the same, but in different directories. To help avoid confusion, from this point on when a file is referred to, it will either be the project file, which is located in the root directory or the app file, which is located in the application's directory.

_example_

- Files in the `WebProject` directory = `project file`
- Files in the `BlogSite` directory = `app file`

## The `settings.py` File

This file is located in the project's directory.

> WebProject<br>
> ┣ BlogSite<br>
> ┃ ┣ migrations<br>
> ┃ ┃ ┗ \_\_init**.py<br>
> ┃ ┣ admin.py<br>
> ┃ ┣ apps.py<br>
> ┃ ┣ models.py<br>
> ┃ ┣ tests.py<br>
> ┃ ┣ views.py<br>
> ┃ ┗ \_\_init**.py<br>
> ┣ WebProject<br>
> ┃ ┣ \_\_pycache**<br>
> ┃ ┃ ┣ settings.cpython-38.pyc<br>
> ┃ ┃ ┗ \_\_init**.cpython-38.pyc<br>
> ┃ ┣ asgi.py<br>
> ┃ ┣ <span style="color:yellow"><font size="4">settings.py</font></span><br>
> ┃ ┣ urls.py<br>
> ┃ ┣ wsgi.py<br>
> ┃ ┗ \_\_init\_\_.py<br>
> ┗ manage.py<br>

<br>
From the Django Docs:

- A Django settings file contains all the configuration of your Django installation. This document explains how settings work and which settings are available.

- A Django settings file doesn’t have to define any settings if it doesn’t need to. Each setting has a sensible default value. These defaults live in the module `django/conf/global_settings.py`.

- If you ever need to see the settings you currently have compared to the default settings you can run the command `python manage.py diffsettings`. This is helpful to see what could have been changed accidentally.

- [read more of the docs here](https://docs.djangoproject.com/en/3.0/topics/settings/)

## Key Sections in the `settings.py` File

### Application Definitions Section

`INSTALLED_APPS = []`

This list represents a list of strings designating all applications that are enabled in this Django installation. Each string should be a dotted Python path to:

- an application configuration class (preferred).
- a package containing an application.

When a Django project is created. The following `INSTALLED_APPS` are added to the list by default:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Key Things To Remember

### All applications that are created will need to be mapped to the `INSTALLED_APPS` list.

## Adding An App To `settings.py`

In order for Django to include the newly created app when the server is ran, it will need to be added to the `INSTALLED_APPS` located in the WebProject(dir) `settings.py` file. The string that needs to be added to this list follows a specific format that maps the app to this list. The format is this:

1\. The name of the app that was created followed by a period. In this guide it is "BlogSite"

2\. After the period, reference the `apps.py` file in the BlogSite directory followed by another period.

_apps.py located here_

> WebProject<br>
> ┣ BlogSite<br>
> ┃ ┣ migrations<br>
> ┃ ┃ ┗ \_\_init**.py<br>
> ┃ ┣ admin.py<br>
> ┃ ┣ <span style="color:yellow"><font size="4">apps.py</font></span><br>
> ┃ ┣ models.py<br>
> ┃ ┣ tests.py<br>
> ┃ ┣ views.py<br>
> ┃ ┗ \_\_init**.py<br>

- The `.py` extension does not need to be added. Django automatically knows the file.

\*apps.py file contains:

```
from django.apps import AppConfig


class BlogsiteConfig(AppConfig):
    name = 'BlogSite'

```

3\. The name of the Class inside the apps.py file is last part of the string

Results = `BlogSite.apps.BlogsiteConfig`

Example of what it looks like in the `settings.py` file:

```python
INSTALLED_APPS = [
    'BlogSite.apps.BlogsiteConfig', # New App Here
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

## The `urls.py` File

Every page you create in your app need its own URL. This way your application knows what it should show to a user who opens that URL. In Django, the URLconf (URL configuration) is used. URLconf is a set of patterns that Django will try to match the requested URL to find the correct view.

The `urls.py` file under the WebProject directory looks like this:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

This was created by Django when the command `django-admin startproject WebProject` was executed.

## How Does Django Process URLs/Request?

_from Django's official documentation_

When a user requests a page from your Django-powered site, this is the algorithm the system follows to determine which Python code to execute:

1. Django determines the root URLconf module to use. Ordinarily, this is the value of the `ROOT_URLCONF` setting, but if the incoming `HttpRequest` object has a `urlconf` attribute (set by middleware), its value will be used in place of the `ROOT_URLCONF` setting.

2. Django loads that Python module and looks for the variable `urlpatterns`. This should be a sequence of `django.urls.path()` and/or `django.urls.re_path()` instances.

3. Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against `path_info`.

4. Once one of the URL patterns matches, Django imports and calls the given view, which is a Python function (or a class-based view). The view gets passed the following arguments:

   - An instance of `HttpRequest`.
   - If the matched URL pattern contained no named groups, then the matches from the regular expression are provided as positional arguments.
   - The keyword arguments are made up of any named parts matched by the path expression that are provided, overridden by any arguments specified in the optional `kwargs` argument to `django.urls.path()` or `django.urls.re_path()`.

5. If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view.

### _layman's terms_

Django will loop through the URLs inside the the `urlpatterns` list inside the urls.py file looking for matches. When a match is found, it will display the page. If there is not a match or the user requesting the page does not have the correct access to view the page, Django will display the response code associated with the error.

#### Key Notes:

- To capture a value from the URL, use angle brackets.
- Captured values can optionally include a converter type. For example, use `<int:name>` to capture an integer parameter. If a converter isn’t included, any string, excluding a / character, is matched.
- There’s no need to add a leading slash, because every URL has that. For example, it’s articles, not /articles.

### Note: A `urls.py` file will need to be created and added to the in the `BlogSite` directory.

## Creating The Apps `urls.py` File

By default, the app that was created does not have a `urls.py` file. In order for Django to render the views from the application, a `urls.py` file needs to be created under the `BlogSite` directory.

_example_

> WebProject<br>
> ┣ BlogSite<br>
> ┃ ┣ migrations<br>
> ┃ ┃ ┗ \_\_init**.py<br>
> ┃ ┣ admin.py<br>
> ┃ ┣ <span style="color:yellow"><font size="4">urls.py</font></span><br>
> ┃ ┣ apps.py<br>
> ┃ ┣ models.py<br>
> ┃ ┣ tests.py<br>
> ┃ ┣ views.py<br>
> ┃ ┗ \_\_init**.py<br>

The file should contain the following:

- The import statements
  - `from django.urls import path`
    - This is to bring in Django's `django.urls.path()` function so it can be used wih the new app like the one used in the WebProject(dir) urls.py file.
  - `from . import views`
    - The period represents the current directory this file is in and its bringing in the views.py file.
- A `urlpatterns` list is also needed, just like the urls.py file in the WebProject directory.

## The `urlpatterns` List

The word `urlpatterns` is actually just a variable that represents a list. That list is a sequence of the `path()` function that was imported in from `django.urls`. Later on there is another function that can be used called `re_path()`.

The `path()` function should follow the syntax below:

```
path(route, view, kwargs=None, name=None)
```

_example_

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
]
```

In the above `urlpatters` list the `path()` function follows the correct syntax.

1. The route is the blank string. This means that just the URL will render the home page.
2. The `views.home` represents that the view is located in the views.py file and the `home()` function is what is executed for the view.
3. The `name='blog-home` is name argument that can be used to also route to this URL.

_Note: If your server is running and you have created this file, you will see an error advising there is no home view since there has not been one created._

---

## Map The New `urls.py` File

Just like new apps need to be mapped to the project - e.g. When `BlogSite.apps.BlogsiteConfig` was added to the `INSTALLED_APPS` list in the settings.py file. The new urls.py file created under BlogSite needs to be mapped to the urls.py file under the WebProject directory.

The urls.py file from the BlogSite directory only needs to be added one time to the WebProject's file but the import statements needs to be modified to import the `include()` function from the `urlpatterns` list.

The file should now look like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('BlogSite.urls')),
    path('admin/', admin.site.urls),
]
```

## The `views.py` File

_from Django's official documentation_

A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.

### _layman's terms_

A view renders your page. They can render something as simple as the dreaded `<h1>Hello World</>` to rendering html templates located within the file system. Views can also handle `code blocks` which perform python code.

## Simple View Example

To follow up on the simple `urlpatterns` list item created above:

```python
urlpatterns = [
  path('', views.home, name="blog-home"),
]
```

A simple view can be created with the name we chose. Inside the urls.py file in the BlogSite directory a new import statement needs to be added. Also a function will need to be created and since the `urlpatterns` above is looking for a function call home, the file should look like this:

```python
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello Newman</h1>')
```

After saving this and running the server. If you navigate to the url provided in your command line you will see a very basic website. At least it wasn't `<h1>Hello World</>`

---

## The `admin.py` File

placeholder

---

## The `views.py` File

---

<br>

# Creating
