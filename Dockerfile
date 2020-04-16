FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt
ENV FLASK_APP=myflasksite.py
CMD ["flask", "run", "--host=0.0.0.0"]
