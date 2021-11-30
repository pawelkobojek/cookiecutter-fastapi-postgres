FROM python:{{cookiecutter.python_version}}

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./{{cookiecutter.package_name}} ./{{cookiecutter.package_name}}
