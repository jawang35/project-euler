# Python

Solutions written in Python 3.6.

## Setup

Setup can be bypassed and tests run by building the Docker image.

```sh
docker build .
```

Alternatively, you can install dependencies and run tests locally.

```sh
make install
```

## Tests

```sh
make test
```

## Run Individual Problem Solutions

```sh
make run problem=[number] # i.e. make run problem=50
```
