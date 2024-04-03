FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./complex_brand_close_collab.py ./invokes.py ./
CMD [ "python", "./complex_brand_close_collab.py" ]