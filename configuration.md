# **Ejecutar comando crear super usuario**

winpty python manage.py createsuperuser

# configuracion de COLLECSTATIC

heroku config:set DISABLE_COLLECTSTATIC=1

# configuracion de DB para migracion de tablas

heroku addons:attach postgresql-acute-23421

# configuracion remoto Heroku 

heroku git:remote -a iranmx2webportfolio
