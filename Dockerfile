FROM python:3.11-slim-buster
COPY . .
ADD main.py .
RUN pip install -r requirements.txt
RUN python3 ./preload.py
CMD python3 ./main.py