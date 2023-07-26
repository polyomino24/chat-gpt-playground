# function-calling

It is well known that ChatGPT cannot do some easy tasks:
- Prime factorization
- Answering today's weather

In this sample project, I help ChatGPT to do prime factorization by using function-calling.

## How to run
```shell
$ export OPENAI_API_KEY=<your key>
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```