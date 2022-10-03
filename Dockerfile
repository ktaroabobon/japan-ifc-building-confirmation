FROM duffn/python-poetry:3.10-slim-1.2.0

WORKDIR /code

COPY api/poetry.lock api/pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pypoetry

COPY api .
COPY jpnifcbc/law jpnifcbc/law
COPY jpnifcbc/wrapper jpnifcbc/wrapper
COPY jpnifcbc/__init__.py jpnifcbc/__init__.py

EXPOSE 8080

ENV PYTHONBUFFERED True

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
