# Gear Store
![Screenshot 2023-12-18 192335](https://github.com/craigrc/gear-store/assets/44074025/03b6f59e-8056-49c7-9b18-70adb03fc99c)
## Description
Gear Store is an application designed to facilitate the lending and borrowing of sports equipment. Users can browse through available gear and make bookings, and this gives admin users a very adequate borrowing history so gear can't go missing!

## Features

### Browsing

![BrowseImages](https://github.com/craigrc/gear-store/assets/44074025/0f5a02ed-d4d5-45e7-ab9b-54a467cc4946)

Categories such as 'harnesses' or 'helmets' can be browsed by users easily.

![View Gear](https://github.com/craigrc/gear-store/assets/44074025/dd9aaf1f-df18-4fa6-89f6-90817796183c)

Clicking on one of these categories reveals details of the category, and allows users to peruse these available items.

![view item](https://github.com/craigrc/gear-store/assets/44074025/be1a0b83-abd7-481e-b781-506ca332bbad)

Choosing one of these items gives information about itself, and whether or not it is available to borrow.

### Profile

![image](https://github.com/craigrc/gear-store/assets/44074025/b4c14400-bd06-4cd4-9185-8c609f634628)

Viewing your profile allows you to see the bookings you have made, and change your details.

### Easily Moddable

![image](https://github.com/craigrc/gear-store/assets/44074025/f33fcde4-529c-415d-a6d9-6a9579b30988)

Popups allow all content that appears to be easily changed to match your brand image.

![image](https://github.com/craigrc/gear-store/assets/44074025/085da211-5c13-4bfd-8fcb-5ba6483a4e9c)
![image](https://github.com/craigrc/gear-store/assets/44074025/d0a73ae4-e8e0-4797-b848-13295e9e7844)

## User Guide
- Make a profile on a hosting server, eg PythonAnywhere.
- Make an app configured as a Django application with Python 3.9.
- Clone the repository to use on a hosting server, eg PythonAnywhere.
- Change your secret code
- Add your hostname to the allowed hosts
- You may need to correct your wsgi.py as follows:
```
"""
WSGI config for groupProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupProject.settings')

application = get_wsgi_application()
```
- Make a virtual environment with
```mkvirtualenv gearstore --python=/usr/bin/python3.9```
- Install necessary libraries with pip install -r requirements.txt
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python populate_gearStore.py
- Configure your static files urls to similar to the following (using your own app name);
![image](https://github.com/craigrc/gear-store/assets/44074025/169bf8b0-4dad-4d1d-b95d-12153ebbacc8)
- Configure your code sources to similar to the following (using your own app name);
![image](https://github.com/craigrc/gear-store/assets/44074025/37d1800a-cc76-4375-9870-2d7f6fe4805d)
- Configure your virtualenv to similar to the following (using your own env name);
![image](https://github.com/craigrc/gear-store/assets/44074025/1a4d21e0-9193-4df5-ad93-247626ab6e63)
- Make an account, and set an admin password from within the account settings.
- Set the url you are hosting from when changing your images, etc.

## Copyright Declaration
This project is based on a University of Glasgow group project submission for Lab Group 10e and has been significantly modiifed with consent to increase usability and the feature set.
