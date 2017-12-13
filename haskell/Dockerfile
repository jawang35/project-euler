FROM haskell:8.0
WORKDIR /opt/project-euler
RUN stack setup

ADD project-euler.cabal /opt/project-euler
ADD stack.yaml /opt/project-euler

ADD . /opt/project-euler
RUN stack test
