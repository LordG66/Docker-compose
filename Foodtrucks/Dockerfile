FROM alpine
WORKDIR /app
RUN apk add --update npm python3 py-pip
COPY ./project/flask-app/ .
RUN npm install 
RUN npm run build; pip install -r requirements.txt
ENTRYPOINT [ "python", "./app.py" ]