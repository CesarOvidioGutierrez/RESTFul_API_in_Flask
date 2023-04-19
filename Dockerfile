FROM python:3.9

WORKDIR /appFlask

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 5000 

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app", "--log-level", "debug", "--access-logfile", "-", "--capture-output"]


