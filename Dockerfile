FROM python:latest

WORKDIR /server

COPY pyproject.toml /server/

RUN apt-get -y update
RUN pip install poetry
RUN poetry install --with dev-dependencies

ENV FLASK_APP=app

COPY ./ /server/


ENTRYPOINT ["poetry", "run", "flask", "run"]
