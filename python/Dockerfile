FROM python:3
WORKDIR /opt/project-euler

COPY Makefile .
COPY setup.py .
COPY requirements.txt .
RUN make install

COPY . .
RUN make test
