FROM python:3.11.4-slim-buster

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat

# Make working directory
RUN mkdir /handballsync
WORKDIR /handballsync

# Copy files
COPY requirements.txt .
COPY ./backend .

# Install dependencies
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./backend/entrypoint.sh .
RUN sed -i 's/\r$//g' /handballsync/entrypoint.sh
RUN chmod +x /handballsync/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/handballsync/entrypoint.sh"]
