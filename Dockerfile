FROM jmrobinson/myflasksite:latest
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN apt update && apt install -y python3-virtualenv
RUN python3 -m venv venv
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
