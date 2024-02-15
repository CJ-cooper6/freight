FROM python:3.9.10-slim-buster
WORKDIR /app
ENV MY_ENV_HOST host.docker.internal
COPY requirements.txt .
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN rm -rf /app/frontend
EXPOSE 5000

CMD ["python", "main.py"]