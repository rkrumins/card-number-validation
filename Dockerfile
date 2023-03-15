FROM python:3.9.16
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV FLASK_APP=/app/server.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4999"]
