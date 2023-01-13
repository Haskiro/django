# Music App. Backend

Web app for listerning music

**Client:**

-  React
-  Redux Toolkit
-  Redux persist
-  TypeScript
-  SCSS
-  antd <br />
[Frontend repository](https://github.com/Haskiro/music-app-frontend)

**Backend:**

-  Django
-  Django REST Framework
-  django-cors-headers
-  django-environ

**Url routes**

-  _/api_ - list of available endpoints
-  _/playlists_ - list of ready playlists.
-  _/artists_ - list of artists.
-  _/genres_ - list of genres.
-  _/tracks_ - list of tracks.
-  _/albums_ - list of albums.
-  _/auth_ - list of users.
-  _/[item]/:id_ - single [item] data.
-  _/auth/login_ - login action (POST method). Response \- access token 
-  _/auth/register_ - registration action (POST method). Response \- access token 

## Quick start

To run the project you need to create virtual environment:
```
python3 -m venv venv
```
And activate it: <br />
for Linux and MacOS
```
source venv/bin/activate
```
for Windows
```
venv\Scripts\activate  
```
Then you need to install dependencies from txt file:
```
pip install -r requirements.txt
```
After installing all the dependencies, the application is launched with the command:
```
python manage.py runserver 127.0.0.1:8000
```
