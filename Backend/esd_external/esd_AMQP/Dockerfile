FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./amqp_setup.py .
RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime
CMD [ "python", "./amqp_setup.py" ]
