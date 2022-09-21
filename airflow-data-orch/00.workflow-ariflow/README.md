# Airflow

## Apache Airflow

- Airbnb 개발
- 2016년 아파치 재단 incubator program
- 아파치 재단 Top Level Project
- Airbnb, Yahoo, Paypal... etc

## Airflow의 사용처

- 데이터 웨어하우스 (DW)
- 머신러닝
- 분석
- 실험
- 데이터 인프라 관리

## 워크플로우 관리 문제

- 매일 주기적으로 돌아가는 데이터 파이프라인이 하나라면 cron script으로 작업을 할 수 있음
- 파이프라인이 여러개가 겹친다면, cron script가 다수로 생성되고 관리가 힘듬
  - 실패복구 -> 언제 어떻게 다시 실행할것인가?
  - 모니터링 -> 잘 돌아가고있는지 확인하기 어려움
  - 의존성 관리 -> 데이터 파이프라인간 의존성이 있는 경우 파이프라인이 심화되어 어려워짐
  - 확장성 -> 중앙화해서 관리하지 않기 때문에 파이프라인 관리가 힘듬
  - 배포 -> 새로운 워크플로우를 배포하기가 힘듬

## 장점

- 워크플로우를 작성하고, 스케줄링, 모니터링 하는 작업을 프로그램이 할 수 있게 해줌
- 파이썬으로 쉽게 프로그래밍 가능
- 분산된 환경에서 확장성이 있음
- 웹 대시보드로 편하게 볼 수 있음
- 커스터마이징 가능

## 워크플로우란?

- 의존성으로 연결된 작업(task)들의 집합
- 의존성으로 연결 된 작업들은 DAG(Directed Acyclic Graph)로 표현

## Airflow는 무엇으로 이루어져 있을까

- 웹 서버 : 웹 대시보드를 제공
- 스케줄러 : DAG를 스케줄링
- Executor : DAG를 실행하기 위한 정의
- Worker : DAG를 실행하기 위한 프로세스
- Metastore : 메타데이터 관리

## DAG(Directly Acyclic Graph)?

- 순환하지 않는 그래프
- 방향성이 한쪽으로만 있는 그래프
  - (A task) -> (B task) -> (C task) : 순환하지 않는 그래프 (DAG)
  - (C task) -> (A task) -> (B task) -> (C task) : 순환하는 그래프

## Operator?

- DAG를 구성하는 하나의 작업
- Operator 종류
  - Action Operators : 실제 연산을 수행
  - Trasnsfer Operators : 데이터를 이동시키는 작업
  - Sensor Operators : 테스크 실행시킬지 정의 / 트리거를 기다림
- Operator를 실행시키면 Task가 됨
- Task = Operator Instance
