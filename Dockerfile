FROM python:3.12

WORKDIR /test-app

COPY . .

RUN pip install -r requirments.txt

EXPOSE 5000



CMD ["python","hello.py"]


