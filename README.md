# The Repo App Project

find repos public for user

## Prepare environment

### Create a virtual environment

```bash
pyenv virtualenv repo_app
pyenv shell repo_app

# or

python -m venv venv
source venv/bin/activate
```

### Install dependency packages

```bash
pip install -r requirements.txt

# for development
pip install -r requirements.dev.txt

# for testing
pip install -r requirements.test.txt
```

### Create Database

If using sqlite, you can pass this step.
This guide intends to help create PostgreSQL db

```bash
sudo apt install postgresql
sudo -u postgres psql
```

```sql
DROP DATABASE IF EXISTS repo_app;

CREATE DATABASE repo_app;

CREATE ROLE repo_app WITH LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE repo_app TO repo_app;
GRANT ALL PRIVILEGES ON SCHEMA public TO repo_app;
ALTER USER repo_app WITH SUPERUSER;
```

### Create environment file

``` bash
cp settings/.env.tpl settings/.env

# Update the environment varables as needed
```

### Run migrate to init database for the app

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

### Install pre-commit

```bash
# cd <TO REPO's root directory>
pre-commit install
```

### Install redis if needed

```bash
# For Ubuntu
## Install redis
sudo apt-get install redis-server
## Start service
sudo service redis-server

# For Mac
## Install redis
brew install redis
## Start service
brew services start redis
```


## Run celery

```bash
ENVIRONMENT=local celery -A celery_tasks worker -l info -Q default
ENVIRONMENT=local celery -A celery_tasks beat -l info
```

## Run flower to easily manage celery in browsers

```bash
# Run flower to manage celery
ENVIRONMENT=local celery -A celery_tasks flower
```


## Run tests

```bash
python manage.py test
```