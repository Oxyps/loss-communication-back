pip install pygdal=="`gdal-config --version`.*"
release: python manage.py migrate
web: gunicorn djangoherokuapp.wsgi --log-file -
