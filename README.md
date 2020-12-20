
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://snip-share.herokuapp.com/)&nbsp;


<h1 align="center">Django_Celery_With_React</h1>

## Introduction
* In this repo, I am creating simple celery app with React using django-rest-framework.
* It will asks you to enter your email address, subject and message, after submit button it will start sending you mail with every 1 minute of interval.

## Technology Stack
* Backend
  * Python
  * Django 
  * Django Rest
* Database
  * SQLite3
* Frontend
  * React
  
## Tech Stack Involved
<div style="display: flex;justify-content: center;">
<img height="64px" width="auto" src="https://image.flaticon.com/icons/svg/919/919852.svg">
 <br/>
<img height="64px" width="auto" src="https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png">
  <br/>
 <img src="https://rawgit.com/gorangajic/react-icons/master/react-icons.svg" width="120" alt="React Icons">
<div/>

## 🚀&nbsp; Setup Instructions
First make sure that you have the following installed.
 * Python 3
 * Node.js
 * Redis MSI
Now do the following to setup project.

First, clone the repository to your local machine:

```bash
git clone  git@github.com:samir321-pixel/Django_Celery_With_React.git
```

# Get Node.js from here
```bash
https://nodejs.org/en/
```

# Get Redis MSI from here
```bash
https://github.com/MicrosoftArchive/redis/releases/download/win-3.2.100/Redis-x64-3.2.100.msi
```

# React Setup:
* Open CMD in following folder
```bash
\Sending_Mail_Using_Celery\frontend\
```

* Hit the following commands
```bash
npm install
```
```bash
npm start
```

# Backend Setup

# Email Setup
* Open File
```bash
Sending_Mail_Using_Celery\settings.py
```
* Enter Your Email details:
```bash
EMAIL_HOST_USER = 'yourgmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
```

# run migrate

```bash
python manage.py migrate
```

# create superuser

```bash
python manage.py createsuperuser
```

# celery Setup
* Open Terminal Window & Hit

```bash
celery -A Sending_Mail_Using_Celery worker -l info
```

* Open New Terminal Window & Hit

```bash
celery -A Sending_Mail_Using_Celery worker -l info
```

# Done!
Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **http://localhost:3000/welcome**.

## 🌏 Browser Support

| <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 10+ | Yes | Yes | Yes |



## Project Admin
[![Maintenance](https://img.shields.io/maintenance/yes/2020?color=green&logo=github)](https://github.com/samir321-pixel)

> **_Need help?_** 
> **_Feel free to contact me @ [saitwalsamir@gmail.com](mailto:saitwalsamir@gmail.com?Subject=Library_Project)_**

## Like This?? Star ⭐ this Repo.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/samir321-pixel/Library_with_Django_Rest)

> Made By Samir Saitwal with ❤️

> Samir Saitwal &copy; 2020
<br><br>
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/samir321-pixel)
[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/samir321-pixel)

***
## Useful Resources
- [Django Docs](https://docs.djangoproject.com/en/3.0/)
- [Django Rest](https://www.django-rest-framework.org/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide)
- [Getting Started – React](https://reactjs.org/docs/getting-started.html)
