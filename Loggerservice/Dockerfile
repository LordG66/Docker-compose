FROM python:alpine
WORKDIR /app
RUN pip install flask
RUN pip install requests
COPY ./logger.py ./logger.py
COPY ./templates ./templates
EXPOSE 8081
ENTRYPOINT [ "python", "logger.py" ]