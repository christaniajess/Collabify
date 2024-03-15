FROM python:3-slim as build
WORKDIR /Project_Post_Service
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./PostProject.py .
CMD [ "python", "./PostProject.py" ]