FROM python:alpine

WORKDIR /app

COPY ./Backend /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

RUN uv sync --locked

EXPOSE 5010

CMD ["uv", "run", "main.py"]


