#!/bin/sh
var=0
while [ "$var" -lt 20 ]
do
    var=$((var+1))
    echo "Esperando conexion a MySQL... $var"
    sleep 2
done


python manage.py makemigrations
python manage.py migrate


gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000
