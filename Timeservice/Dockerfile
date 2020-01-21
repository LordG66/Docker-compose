FROM python:alpine
WORKDIR /app
RUN pip install flask
COPY ./timeapp.py ./timeapp.py
COPY ./templates ./templates
EXPOSE 8080
ENTRYPOINT [ "python", "timeapp.py" ]