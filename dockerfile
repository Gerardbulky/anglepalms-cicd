FROM python:3.9
WORKDIR /angelpalms
COPY ./requirements.txt /angelpalms/
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
