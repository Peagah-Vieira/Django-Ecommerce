[![Python 3.11](https://img.shields.io/badge/python-3.11-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.2](https://img.shields.io/badge/Django-4.2-green.svg)
# Django Ecommerce

## Running locally

Clone the project

```bash
git clone  https://github.com/Peagah-Vieira/Django-Ecommerce
```

Create a virtual environment

```bash
# Linux
sudo apt-get install python3-venv    
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

Update the pip

```bash
py -m pip install --upgrade pip
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Copy the example env file and make the required configuration changes in the .env file

```bash
cp .env-example .env
```

Perform the migrations

```bash
py manage.py migrate
```

Create a superuser
```bash	
py manage.py createsuperuser --email admin@example.com --username admin
```

Start the server

```bash
py manage.py runserver
```

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Django Restframework](https://www.django-rest-framework.org)

[Django Restframework-SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)