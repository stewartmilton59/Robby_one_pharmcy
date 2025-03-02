#!/usr/bin/myenv bash

#exiting on error
set -o errexit

#Modify this line as needed for your package manage (pip, poetry, etc.)
pip install -r requirements.txt

# convert static asses files
python manage.py collectstatic --no-input
python3 manage.py collectstatic --no-input

#apply any outstanding database migration
python manage.py migrate
python3 manage.py migrate