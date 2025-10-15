FROM python:3.12.3

WORKDIR /healthcare

COPY . /healthcare

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "app/main.py"]

