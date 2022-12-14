FROM ubuntu:20.04
RUN apt update
RUN apt upgrade -y
RUN apt install sqlite3 -y
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pytest
RUN pip install black
RUN pip install flake8
RUN pip install isort
RUN pip install mypy
RUN pip install web.py
RUN pip install pyrebase