FROM python:3.9.1-slim

ENV APP_HOME /APP_HOME
WORKDIR ${APP_HOME}

COPY . ./   
#copy whats in serverless-django dir and copy into /app dir

RUN pip install pip pipenv waitress --upgrade
RUN pipenv install --skip-lock --system --dev

# CMD ["./scripts/entrypoint.sh"]
CMD DJANGO_SETTINGS_MODULE=serverless_django.settings.production waitress-serve --listen=0.0.0.0:$PORT serverless_django.wsgi:application 
