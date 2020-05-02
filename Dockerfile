FROM python:3.8-slim-buster
WORKDIR /myapp
COPY . /myapp
ENV FLASK_APP=main.py
RUN pip3 install -r requirements.txt
VOLUME /myapp
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

