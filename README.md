# safepassage_server
Following things need to be taken care of when setting up the host machine:
1. Git deployment action has HOST ip address
2. Host machine's ssh key needs to be added as deployment key in repo
3. Host machine's environment needs DBHOST and DBPASS in /etc/environment
4. Apache should be configured to run a wsgi application

```
WSGIDaemonProcess safepassage.vics python-path=/home/mayankbhagya/safepassage_server/COVIDSafepassage/
WSGIProcessGroup safepassage.vics

WSGIApplicationGroup %{GLOBAL}

WSGIScriptAlias / /home/mayankbhagya/safepassage_server/COVIDSafepassage/COVIDSafepassage/wsgi.py

<Directory /home/mayankbhagya/safepassage_server>
Require all granted
</Directory>
```