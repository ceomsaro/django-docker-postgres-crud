#!/bin/sh

echo "⏳ Esperando a que Postgres esté listo..."
until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  sleep 2
done

echo "🔄 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🚀 Levantando servidor..."
python manage.py runserver 0.0.0.0:8000
