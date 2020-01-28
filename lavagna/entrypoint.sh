#!/bin/sh
while !wget http:///mysql:3306; do
    sleep 1
done
java -Xms64m -Xmx128m -Ddatasource.dialect="${DB_DIALECT}" \
-Ddatasource.url="${DB_URL}" \
-Ddatasource.username="${DB_USER}" \
-Ddatasource.password="${DB_PASS}" \
-Dspring.profiles.active="${SPRING_PROFILE}" \
-jar /lavagna/target/lavagna-jetty-console.war --headless
