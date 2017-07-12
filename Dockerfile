FROM python:2.7
MAINTAINER Vyacheslav Tykhonov "vyacheslav.tykhonov@dans.knaw.nl"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
