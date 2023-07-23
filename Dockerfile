FROM python:3.10

WORKDIR /accounts-api

COPY requirements.txt /accounts-api
COPY . ./accounts-api


RUN pip install --no-cache-dir --upgrade -r /accounts-api/requirements.txt

CMD ["uvicorn", "accounts-api.main:app", "--host", "0.0.0.0", "--port", "80"]