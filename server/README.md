# Synchron
Python Django based web app that facilitates the maintenance and synchronization of daily standups in any scrum team.

# Requirements
 - Docker

## Usage.
---
1. Build and run docker container. (Remove build flag if you are not running this project for the first time)
```
    docker-compose up --build
```

2. Stop Container
```
    docker-compose down
```

The develpoment server starts at http://127.0.0.1:8000.

## If you are running this project for the first time, make sure to migrate models.
To do that, First you must SSH into running container.
```
    docker exec -it django_web sh
```

then run following commands:
```
    python manage.py migrate
```



## You can access API docs at
http://127.0.0.1:8000/swagger


## Liscense
MIT