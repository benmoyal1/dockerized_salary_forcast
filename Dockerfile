FROM python:3.10
ENV PYTHONDONTRUNBYCODE 1
ENV PYTHONUNBUFFERED 1 
WORKDIR /code 
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
COPY . /code/