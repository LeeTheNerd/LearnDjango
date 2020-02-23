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

```
A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
```

### _layman's terms_

All Django projects begin with a project. The project is the root folder for everything associated with the project including apps. Django will create this folder with the name specified in the `django-admin` command.

In the code example below. The project is called 'BlogSite'

`django-admin startproject BlogSite`

This will create the following project in the file system as the root directory.

```
BlogSite/
┣ BlogSite/
┃ ┣ __init__.py
┃ ┣ asgi.py
┃ ┣ settings.py
┃ ┣ urls.py
┃ ┗ wsgi.py
┗ manage.py
```

**Make sure you navigate into this directory**

Think of this directory as the server. You can run this server but there is no content associated with it. However, this is now a fully functional web server that can be started from the `manage.py` file.

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

```
An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app
```

### _layman's terms_

Think of an app as the website being hosted on the server. One app can be the entire website - e.g., a static 1 page site. Apps can also be components that combine with other apps within a project that create an entire website - e.g., main site, ecommerce page, users, etc.
