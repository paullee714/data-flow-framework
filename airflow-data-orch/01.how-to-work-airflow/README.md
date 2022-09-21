# Airflow의 구조, DAG의 실행 및 생성

## Airflow의 환경

1. 하나의 서버에서 실행되는 One Node Architecture
2. 분산된 환경에서 실행되는 Multi Node Architecture

## One Node Architecture

- 구성요소
  - Web Server
  - Metastore
  - Scheduler
  - Executor

- Metastore 는 Dag에 대한 정보를 담고 있음
- Web Server와 Scheduler는 Metastore를 읽어와서 Executor에게 전달
- Executor는 전달받은 Task를 실행
- Executor는 실행 결과를 Metastore에 저장, Web Server와 Executor가 다시 읽어올 수 있음

- Executor는 Queue가 존재 
    - Multi Node와 One Node의 큰 차이점 중 하나
    - Celery Broker가 존재
    - Master Node에서 Airflow UI, Scheduler가 존재
    - Master Node에서 Celery 로 Task를 전달
    - Worker Node에서 Celery 에 있는 Task를 실행


## DAG의 생성과 실행
- user가 새로운 DAG를 작성 후 Folder Dags에 저장
- web server가 Scheduler에서 읽어옴
- Scheduler가 Metastore를 통해 DagRun(DAG Instance) 오브젝트 생성
- Task Instance 오브젝트를 스케줄링
- Task Instance를 Executor로 보냄
- 완료 후 Executor는 Metastore에 보고
- Scheduler는 DAG 실행이 완료되었나 확인
- UI 에서 업데이트