FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./app.py .
RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime
CMD [ "python", "./app.py" ]
