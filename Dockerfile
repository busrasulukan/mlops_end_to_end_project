FROM python:3.9.18-slim-bullseye

RUN mkdir code/

WORKDIR code/

COPY . . 

RUN pip install update pip && pip install -r requirements.txt

EXPOSE 8080

CMD [ "uvicorn","main:app", "--host=0.0.0.0","--port=8080" ]