FROM python:3.9

RUN pip install flask

COPY . /calc

WORKDIR /calc

CMD ["python", "calc.py"]