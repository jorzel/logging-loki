FROM python:3.9-slim
RUN apt-get update && apt-get install build-essential -y
COPY app.py requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 8082
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8082"]