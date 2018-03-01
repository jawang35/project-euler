FROM haskell:8.0
WORKDIR /opt/project-euler
RUN stack setup 8.0

COPY project-euler.cabal .
COPY stack.yaml .

COPY . .
RUN stack test
