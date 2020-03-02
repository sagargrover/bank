# Bank

Banking system to handle transactions and impose validity checks

## Getting Started


### Run on Docker

This project can be run as standalone app using docker.

```
docker image build -t bank:2.0 .

```
To run docker image, use this command to enter bash mode
```
docker run --entrypoint "bash" -it bank:2.0

```
You can change input.txt and run command
```
python app.py < input.txt > output.txt

```
to see output

### Run on local machine

Needs virtual env and python3.7 for dependencies

```
virtualenv --python=/usr/local/Cellar/python@3.7/3.7.6/bin/python3.7 venv
source venv/bin/activate
pip install -r requirements.txt

```
To run app with input file as input.txt and output file as output.txt
```
python app.py < input.txt > output.txt

```
## Running the tests

Tests for all the modules are enclosed in test/ folder


To verify tests run
```
python -m unittest discover -s test/ -p '*_test.py'
```

## Config
To alter window size and time for validity checks, edit config.yml with corresponding params
