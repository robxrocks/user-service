FROM python:3.7-alpine
MAINTAINER Rob Rokosz <rr.t3ch@gmail.com>

WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./user_service .

CMD ["flask", "run"]