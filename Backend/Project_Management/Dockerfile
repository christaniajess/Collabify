FROM python:3-slim as build
WORKDIR /Project_Management
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./project.py .
CMD [ "python", "./project.py" ]
