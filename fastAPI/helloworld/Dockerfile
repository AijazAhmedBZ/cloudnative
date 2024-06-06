FROM python:3.12
RUN pip install poetry
LABEL MAINTAINER="aijaz.ahmed.bz@gmail.com"
WORKDIR /code
COPY ./pyproject.toml ./helloworld /code/
COPY ./helloworld /code/helloworld/
RUN poetry install
ENTRYPOINT [ "poetry", "run", "uvicorn", "helloworld.main:app", "--host", "0.0.0.0" ]