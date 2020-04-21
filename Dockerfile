FROM python:3.7-slim-buster
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
