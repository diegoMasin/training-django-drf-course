![Alt text](https://raw.githubusercontent.com/diegoMasin/landing-maximumtech/master/assets/img/new-logo-mt-01.png)
<br><br>

# Django + Django Rest Framework (Template)

###### Training Django Rest Framework with best practices.

## Requirements

- Python (choose your version)

## Install Project

```
- on this template repository, click on 'Use this template'
- clone the new repository
- cd <project-folder>
- python -m venv .venv
- source .venv/bin/activate
- change the requirements.txt file if you don't want to get the latest versions
- pip install -r requirements.txt
- change file putting installed versions to fix versions.
- change the 'backend' name to the name of your project throughout the project (if you wish)
    - não altere no settings.py onde tem 'BACKEND' e 'backends'
    - do not change anything in the .env, env_gen.py and README.md files
- do the same for the 'core' name if you want your first app to have another name (if you wish)
    - change only the files: asgi.py, settings.py, wsgi.py and apps.py files
- python contrib/env_gen.py
- rm -rf contrib
- python manage.py migrate
- python manage.py createsuperuser --username="admin" --email=""
```
