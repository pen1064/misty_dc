From python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . /app/

RUN pip install numpy==1.21.5
RUN pip install pandas==1.3.5
RUN pip install scikit_learn==1.0.2
RUN pip install xgboost==1.5.1
RUN pip install Django==4.0.1
RUN pip install djangorestframework==3.13.1


WORKDIR /app

