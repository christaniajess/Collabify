FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./place_request.py ./invokes.py ./amqp_connection.py ./
CMD [ "python", "./place_request.py" ]
