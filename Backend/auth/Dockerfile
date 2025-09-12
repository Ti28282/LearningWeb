FROM python:alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /work

COPY . .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

RUN uv sync --locked

EXPOSE 5010

CMD ["uv","run","app/main.py"]


