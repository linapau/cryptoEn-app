# cryptoEn
## About the project

Python, Django framework
 
**##Firebase:**
- Created Realtime Database (server, private key)
- Created Storage - its storage for our files
- Firestore Database - I think that we actually do not need this
- If not necessary, do NOT change anything in Firebase

**##Upload, download**
- Run server: py manage.py runserver
- Upload: /upload_file
- Download: /browse_files
- If want to login as admin, before runserver: py manage.py createsuperuser
- Superuser should be set but sometimes it gets deleted, I don't know why (we dont need this anyway but if didnt delete, User: kamil, password: admin) /admin

**##Backend Structure**
project/
├── data/
│   ├── models/
│   ├── views/
│   │   ├── views_user.py
│   │   └── views_file.py
│   ├── serializers/
│   ├── admin.py
│   ├── firebase.py
│   ├── urls/
│   │   └── urls.py
│   └── ...
│ 
├── ssd_encryption/
│   ├── templates/
│   │   └── data/
│   │       └── upload_file.html
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│ 
├── manage.py

sddd
