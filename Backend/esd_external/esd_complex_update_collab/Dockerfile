FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./app.py ./invokes.py ./amqp_connection.py ./
CMD [ "python", "./app.py" ]
