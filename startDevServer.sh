#!/bin/bash

export APPNAME='PackageBazaar'
export TIME_ZONE='Europe/Zurich'
export LANGUAGE_CODE='en-us'
export ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
export DEBUG=1
export MUNKI_REPO_URL='file:///Users/Shared/munki_repo'
export MUNKITOOLS_DIR='/usr/local/munki'

# Start the development server
python manage.py runserver