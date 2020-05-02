FROM python:3.8-slim-buster
RUN mkdir /test
WORKDIR /test
COPY . /test
RUN pip3 install -r requirements.txt
VOLUME /test
CMD ["python3", "test.py"]
