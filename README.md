## adjust-task

-----    
    
### Introduction

This is a simple single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. 
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, 
advertising channel, country and operating system.

### Tech Stack

Our tech stack will include:

* **Python3** and **Django** as our server language and server framework
* **Django REST framework** for building the API
* **PostgreSQL** as our database of choice
* **Docker** , **Docker Compose** Application containerization 


### Main Files: Project Structure
```sh
├── analysis
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   └── seed_data.py
│   │   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
└── requirements.txt
```

## Quick start

To run the project locally,

1. Open a terminal:
  ```shell
  git clone https://github.com/HamdyTawfeek/adjust_home_task.git
  cd adjust_home_task
  docker-compose up
  ```

2. Navigate to Home page [http://localhost:8000/api/v1/metrics/]( http://localhost:8000/api/v1/metrics/)


## Future enhancements

1. Add test cases for the API