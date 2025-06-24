FROM python:3.11-slim
WORKDIR /app
COPY Scriptpython.py .
RUN python -m pip install --upgrade pip
RUN pip install pylint
RUN python -m unittest Scriptpython
RUN pylint Scriptpython.py
