FROM python:3.7.3-slim
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/app/
EXPOSE 8080
WORKDIR /opt/app
CMD gunicorn -w 8 views:APP --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker --log-level=DEBUG