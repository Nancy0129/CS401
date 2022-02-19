FROM python:3.7-slim
RUN mkdir /try0


COPY try.py /try0
COPY ML.pickle /try0
COPY TF.pickle /try0
COPY CV.pickle /try0
COPY requirements.txt requirements.txt
WORKDIR /try0

RUN pip install -r requirements.txt 

ENTRYPOINT ["flask","run","--port","5001"]




