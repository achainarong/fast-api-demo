FROM python:3.11.3-alpine3.17

ENV POETRY_VERSION=1.4.2

RUN mkdir /app
WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0" , "--port", "8000"]