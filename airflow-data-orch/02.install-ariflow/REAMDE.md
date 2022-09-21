# Airflow Installation

## Python 설치 환경 준비

1. Anaconda
2. Python Virtual Environment

여기서 나는, Python Virtual Environment를 사용할 것이다.

## Python Virtual Environment 실행

- poetry
  ```shell
  $ poetry init
  $ poetry shell
  ```
- venv
  ```shell
  $ virtualenv venv --python=python3.10
  ```

## Airflow Package 설치

- Run Virtual environment

  - poetry
    ```shell
    $ poetry shell
    ```
  - venv
    ```shell
    $ source venv/bin/activate
    ```

- Install Airflow
  - poetry
    ```shell
    $ poetry add apache-airflow
    ```
  - venv
    ```shell
    $ pip install apache-airflow
    ```

## Airflow DB 초기화

- airflow를 실행하기 전에, airflow DB를 초기화 해야한다.
- 명령어 실행
  ```shell
  (venv) $ airflow db init
  ```

## Airflow User 생성

- airflow를 실행하기 전에, airflow user를 생성해야한다.
- 명령어 실행
  ```shell
  (venv) $ airflow users create \
      --username admin \
      --firstname admin \
      --lastname admin \
      --role Admin \
      --email admin@mail.com
  ```

## Airflow Webserver 실행

- airflow db init이 끝났다면, webserver를 실행시켜 UI를 확인하자
- 명령어 실행
  ```shell
  (venv) $ airflow webserver -p 8080
  ```
