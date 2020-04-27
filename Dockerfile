FROM jmrobinson/myflasksite:latest
WORKDIR /myapp
COPY . /myapp
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
