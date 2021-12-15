## Create virtual environment & initialize a git repo
If this has not been done when the web app was created, you can create a new folder & do these steps, & then migrate the code files from your web app into here.
```
sudo apt install -y python3-venv   --> Install a python virtual environment builder

cd <to your desired project folder location>
mkdir PythonApp
cd PythonApp

python3 -m venv django_env      --> Create a virtual env named django_env
source django_env/bin/activate  --> Activate the virtual env

pip install django OR flask 

git init
```
<br/>

## Create the Flask/Django app
...Assuming that this part isn't an issue, because it should not affect the deployment.

<br/>

## First time Deploying
```
pip install gunicorn
```


---


Flask: Create a `Procfile` file with this command. The `<app>` is the name of your Flask .py file containing the `app.run()` command.
```
echo "web: gunicorn app:<app>" > Procfile
```
  
  
Django: Create a `Procfile` file with this command. The `<app>` is the name of your Django Project Admin folder that you created using the `django-admin startproject <app>` terminal command at the very start.
```
echo "web: gunicorn <app>.wsgi" > Procfile
```


Django: Install this library to do the background work for deploying Django to Heroku
```
pip install django-on-heroku  
```  
  
  
Django: At the top of `settings.py` add the following statement.
```
import os
import django_on_heroku
```
  
  
Django: At the end of `settings.py`, add the following statement.
```
STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)
  
# Activate Django-on-Heroku.
django_on_heroku.settings(locals())
```
  
  
---
  
  
Flask: In `app.py`, turn `debug=True` to false
```
if __name__ == "__main__":
    app.run(debug=False)
```
  
  
Django: In `settings.py`
```
DEBUG = False

ALLOWED_HOSTS = ['https://<heroku-project-name>.herokuapp.com/', 'localhost', ' 127.0.0.1']
```

  
Create `requirement.txt` to state all the dependencies of the project, & commit the project.  
```
pip freeze > requirements.txt
git init
git add .
git commit -m "Deploy to Heroku"
```
  
  
Install Heroku CLI (if not done so yet), and login to Heroku
```
curl https://cli-assets.heroku.com/install.sh | sh
heroku login      --> opens in browser after pressing any key
heroku -h         --> check if Heroku is working locally
heroku create <projectName>   --> Create a project in Heroku for the app
git push heroku master        --> Push project to Heroku to deploy
```
  
  
Django: Extra step after pushing project to Heroku
```
heroku run python manage.py migrate  
```
  
  
Open the deployed app in browser
```
heroku open OR click the link
```
  
  
  
## Redeploying app

Turn `DEBUG=False` again

  
If got new pip installs, 
```
pip freeze > requirements.txt
```
  
  
Push local changes to Heroku project
```
git add .
git commit -m "New Deploy"
git push heroku master
```
