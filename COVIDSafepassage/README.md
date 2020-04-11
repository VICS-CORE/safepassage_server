#safepassage_server

##Dependency

* Python : 3.7.4
* Django : 3.0.4
* djangorestframework : 3.11.0
* mysql : 0.0.2
* mysqlclient : 1.4.6

### LocalSetup
* ```$ git clone  https://github.com/VICS-CORE/safepassage_server.git```
* Install dependencies. Note: I used MySQl for Database. Please make sure you have MySql installed.
* ```$ python manage.py makemigrations```
* ```$ python manage.py migrate```

Note: It is using a local Database, so create a supersuer.
* ```$ python manage.py createsuperuser```
Then
* ```$ python manage.py runserver```
* Access localhost............./admin
* Login
