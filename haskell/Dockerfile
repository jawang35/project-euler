FROM haskell:8
WORKDIR /opt/project-euler

ADD project-euler.cabal /opt/project-euler
ADD stack.yaml /opt/project-euler
RUN stack setup

ADD . /opt/project-euler
RUN stack test
