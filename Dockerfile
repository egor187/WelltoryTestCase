FROM python:3.10.0 as dependecies

COPY requirements.txt /requirements.txt

WORKDIR /WelltoryTestCase

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt


FROM dependecies

COPY . /WelltoryTestCase

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /WelltoryTestCase

WORKDIR /WelltoryTestCase

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]