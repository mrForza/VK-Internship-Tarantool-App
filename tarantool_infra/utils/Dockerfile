FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY /poetry.lock /pyproject.toml ./

RUN poetry --version
RUN poetry install --no-interaction --no-cache

COPY . /app

ENV PYTHONPATH=src

EXPOSE 8088

CMD ["poetry", "run", "python", "-m", "main"]