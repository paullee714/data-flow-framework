# Airflow Database

- Airflow는 기본적으로 sqlite를 사용
- Sequnetial Executor만 사용하면, sqlite를 사용해도 된다.
- 하지만 다른 Executor를 사용한다면 DB변경이 필요하다.
- 좀 더 넓은 범위의 사용을 위해, Postgresql를 사용할 것이다.

## DB(postgresql) 설치

- 간단하게 docker-compose로 설치 할 것
- 설치 방법은, [링크](https://www.wool-dev.com/data-engineering/database/database-with-docker) 를 참고하거나 아래의 명령어들을 따라 실행

### Docker

- Docker를 설치 해 준다
- [링크](https://docs.docker.com/engine/install/) 참고

### Docker compose file 생성 및 실행

- docker-compose.yml 파일 생성

  ```yaml
  version: "3.9"

  services:
    postgres:
      image: postgres:14-alpine
      ports:
        - "5432:5432"
      volumes:
        - .postgresql/:/var/lib/postgresql/data
      environment:
        - POSTGRES_PASSWORD=admin
        - POSTGRES_USER=admin
        - POSTGRES_DB=airflow
  ```

- docker-compose.yml 실행
  ```shell
  $ docker-compose up -d
  ```

## Airflow 설정
- airflow 실행 전, airflow.cfg 파일을 수정 해 준다.
- airflow를 설치했다면, home 디렉터리에 생성이 되었을텐데, 나는 맥 m1에 설치했기 때문에 경로는 `~/airflow` 에 있다
- 해당하는 디렉터리에서 `airflow.cfg` 파일을 수정해 준다.
- 위에 설정한 `POSTGRES_PASSWORD`, `POSTGRES_USER`, `POSTGRES_DB`를 airflow에 아래와 같이 넣어준다
    - sql_alchemy_conn = postgresql+psycopg2://admin:admin@localhost/airflow
    - result_backend = db+postgresql://admin:admin@localhost/airflow

### 에러가나는데요?
- psycopg2를 설치해 준다
    ```shell
    $ pip install psycopg2
    ```
- 일부 컴퓨터에서 psycopg2 설치 오류가 날 수 있다
- [여기](https://stackoverflow.com/questions/66888087/cannot-install-psycopg2-with-pip3-on-m1-mac) 를 참고해서 해결했다


## Airflow 초기화 및 실행
- airflow 설정을 초기화해주었기 때문에 다시 한번 실행 해 준다
    ```shell
    $ airflow db init
    ```

- airflow scheduler 실행
    ```shell
    $ airflow scheduler
    ```

- airflow를 실행해 준다
    ```shell
    $ airflow webserver -p 8080
    ```

