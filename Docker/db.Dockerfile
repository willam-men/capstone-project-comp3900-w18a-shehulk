FROM postgres:14.5-1
COPY init.sql /docker-entrypoint-initdb.d/