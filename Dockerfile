FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./fastapi-mnist /code/fastapi-mnist
CMD ["uvicorn", "fastapi-mnist.main:app", "--host", "0.0.0.0", "--port", "80"]
