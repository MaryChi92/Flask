FROM python:3.8.10-buster

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache --user -r requirements.txt

COPY . .

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

#EXPOSE 5000

#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]