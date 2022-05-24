# Airflow 개념정리 및 예제만들기

## 주요 명령어
- `docker-compose up airflow-init`
- `docker-compose up`
- `docker-compose down --volumes --rmi all`


### 설치하기
- [Airflow](https://airflow.apache.org/installation.html)는 데이터엔지니어링에서 많이 쓰이는 프레임워크 중 하나이다.
- local로 설치하거나, Kubernetes에서 설치를 할 수 있다
    - local로 설치 할 경우, docker-compose를 사용해서 한번에 구축하는것이 가장 편하다
- 나의 경우에는 `docker-compose`가 편해서 airflow 공식문서에서 제공하는 파일로 설치하려고한다

### docker-compose파일 받기
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml'
```
- 위의 파일은, airflow에서 직접 작성한 docker-compose 파일이다
- 위의 파일을 사용해서 airflow를 local 환경에서 docker로 올리려고한다

### docker-compose -> airflow 설정 초기화
- airflow를 실행하기 위해 환경 세팅 및 데이터베이스 세팅이 필요하다
- airflow docker-compose 파일 내부에 해당하는 설정 작업들이 세팅되어있다
- 아래의 명령어를 사용해서 docker-compose를 실행하면 airflow 세팅이 가능하다
    ```bash
    docker-compose up airflow-init
    ```
- 아래와 같은 문구가 터미널에 출력되면 세팅이 완료 된 것
    ```bash
    docker-with-airflow-airflow-init-1  | Admin user airflow created
    docker-with-airflow-airflow-init-1  | 2.1.1
    docker-with-airflow-airflow-init-1 exited with code 0
    ```

### docker-compose -> airflow 실행하기
- 이전에 실행 한 것은 airflow 실행을 위한 환경 및 폴더, DB세팅들을 진행 한 것
- 아래의 명령어로 airflow를 실행시켜 준다
    ```bash
    docker-compose up
    ```
- airflow가 실행되는데 시간이 조금 걸린다. 커피한잔 하고 오면 된다
- 생성된 application에 `http://localhost:8080/` 으로 접속을 하면 됨
- 접속시, admin계정이 필요하다. ID/PW에 모두 `airflow`를 적어주면 된다

### 생성되는 docker container 및 각 container 역할
- docker-compose로 실행 한 airflow 컨테이너들은 아래와 같이 생성된다
    - docker-with-ariflow-airflow-init-1
        - airflow 환경세팅 컨테이너
    - docker-with-airflow-postgres-1
        - postgres 데이터베이스
    - docker-with-airflow-redis-1
        - 스케쥴러에서 작업자로 메시지를 전달하는 브로커
    - docker-with-airflow-airflow-worker-1
        - 스케쥴러에서 제공한 작업을 실행하는 작업자
    - docker-with-airflow-airflow-scheduler-1
        - 모든 작업, DAG을 모니터링하는 스케쥴러
        - 조건과 일치하는 작업을 실행
    - docker-with-airflow-flower
        - 환경 모니터링을 위한 앱
    - docker-with-airflow-airflow-webserver-1
        - airflow를 확인 할 수 있는 웹서버(admin)


### future work
- 더미데이터 생성 모듈을 만들어서, airflow가 활용 할 수 있도록 해봐야겠다
- DAG, Plugin 들을 활용 해 보려고 한다