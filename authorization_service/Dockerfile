FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY /src/poetry.lock /src/pyproject.toml ./

RUN poetry --version
RUN poetry install --no-interaction --no-cache

COPY . /app

ENV PYTHONPATH=src

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "src.main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8080"]