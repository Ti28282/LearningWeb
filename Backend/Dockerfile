FROM python:alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./Backend .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

RUN uv sync --locked

EXPOSE 5010

CMD ["uvicorn", "app:app", "--port", "5010", "--host", "0.0.0.0"]


