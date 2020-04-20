# safepassage_server
Following things need to be taken care of when setting up the host machine:
1. Git deployment action has HOST ip address
2. Host machine's ssh key needs to be added as deployment key in repo
3. Host machine's environment needs DBHOST and DBPASS in /etc/environment
4. Apache should be configured to run a wsgi application
