#!/bin/bash

echo "Starting deploy.sh...", $(date)
pushd ~/safepassage_server/COVIDSafepassage
git pull
python3.6 manage.py migrate
touch COVIDSafepassage/wsgi.py
popd
echo "Done"
