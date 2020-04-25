#!/bin/bash

echo "==== Starting deploy.sh...", $(date)
pushd ~/safepassage_server/COVIDSafepassage
git stash
git pull
git stash pop
echo "==== Installing python dependencies..."
pip3 install -r requirements.txt
echo "==== Applying migrations..."
python3.6 manage.py migrate
echo "==== Restarting apache..."
touch COVIDSafepassage/wsgi.py
popd
echo "==== Done"
