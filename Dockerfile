FROM python:latest
COPY /manager .
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY manager server

# Code du prof :
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /
RUN chmod +x /wait-for-it.sh

#CMD [“python -m .”, “devoir2”]
CMD python -m server
EXPOSE 3210

ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--"]

# CMD ["python", "-m", "server"]

