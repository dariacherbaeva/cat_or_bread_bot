FROM python:3.9
LABEL maintainer='dariacherbaeva'

ENV PYTHONUNBUFFERED 1

COPY ../requirements.txt /tmp/requirements.txt
COPY ../api /api
WORKDIR /api
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        cat-bread-user

ENV PATH="/py/bin:$PATH"

USER cat-bread-user
