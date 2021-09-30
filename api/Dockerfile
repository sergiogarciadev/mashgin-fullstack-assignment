FROM python:3.9

WORKDIR /app

COPY setup.py .
COPY shopping_api/ shopping_api/
COPY migrations/ migrations/

RUN pip install -e .[prod]

CMD [ "gunicorn", "--bind=0.0.0.0:80", "shopping_api:app" ]
