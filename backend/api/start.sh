#!/bin/sh

echo "Waiting database"

while ! nc -z db 5432; do
	sleep 0.1
done

echo "Database up"

echo "Start app"

uvicorn main:app --host 0.0.0.0 --port 5000

