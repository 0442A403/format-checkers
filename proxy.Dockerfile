FROM python:latest

WORKDIR /server

COPY pyproject.toml /server/

RUN apt-get -y update
RUN pip install poetry
RUN poetry install --with dev-dependencies

EXPOSE 2000
ENV FLASK_APP=proxy

COPY ./ /server/

ENTRYPOINT ["poetry", "run", "flask", "run"]