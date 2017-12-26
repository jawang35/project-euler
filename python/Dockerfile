FROM python:3
WORKDIR /opt/project-euler

ADD setup.py /opt/project-euler
RUN python3 setup.py install

ADD requirements.txt /opt/project-euler
RUN pip3 install -r requirements.txt

ADD . /opt/project-euler
RUN pep8 . && PYTHONPATH=/opt/project-euler py.test -v --color=yes --durations=20
