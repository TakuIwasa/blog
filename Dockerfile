FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN apt-get update -y
RUN apt-get install nginx -y

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:80", "--settings", "config.settings.production"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--access-logfile",  "-", "--capture-output", "config.wsgi"]