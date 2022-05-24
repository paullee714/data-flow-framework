# Spring Data Flow 시작해보기
- Spring에서 꽤나 많은 기능들을 미리 제공하고있어서 각각의 프레임워크들, 기능들을 하나씩 사용 해 보던 중 `Spring-Cloud-Data-Flow`라는 것을 알게되었다
- Spring Cloud Data Flow를 사용해서 데이터처리 파이프라인을 구성 해 보고자 한다
- 우선 설치방법, 세팅방법을 정리하고, 하나씩 프로젝트를 만들어 나가려고한다

## 설치방법
- [공식문서](https://dataflow.spring.io/getting-started/)를 참고했다
- 로컬환경에서 충분히 운영 할 수 있겠다고 판단했다

### Download Jars
- 매뉴얼에 나와있는대로, Data Flow Server jar파일을 먼저 설치하자
    ```bash
    wget https://repo.spring.io/release/org/springframework/cloud/spring-cloud-dataflow-server/2.9.2/spring-cloud-dataflow-server-2.9.2.jar
    
    wget https://repo.spring.io/release/org/springframework/cloud/spring-cloud-dataflow-shell/2.9.2/spring-cloud-dataflow-shell-2.9.2.jar
    ```
- Skipper라는 서버가 있는데, 이것또한 jar파일을 받아주자 
    ```bash
    wget https://repo.spring.io/release/org/springframework/cloud/spring-cloud-skipper-server/2.8.2/spring-cloud-skipper-server-2.8.2.jar
    ```

### Message Application 설치 
- 원래 설치가 되어있다면 설정값들을 기억 해 주고 사용하자
- 그렇지 않다면, 공식문서에 나온대로 `docker`를 사용해서 `rabbitMQ`를 설치 해 주도록 하겠다
- RabbitMQ 설치 및 실행
    ```bash
    docker run -d --hostname rabbitmq --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3.7.14-management
    ```
- 나는 M1 Macbook이라 `arm64v8` 태그로 설치했다
    ```bash
    docker run -d --hostname rabbitmq --name rabbitmq -p 15672:15672 -p 5672:5672 arm64v8/rabbitmq
    ```

## 서버 실행하기
- 위의 설치과정이 정상적으로 완료되었다면 다운받은 JAR파일을 실행하여 서버를 실행 해 주도록 하자

### skipper 서버 실행하기

```bash
java -jar spring-cloud-skipper-server-2.8.2.jar
```

### data flow 서버 실행하기

```bash
java -jar spring-cloud-dataflow-server-2.9.2.jar
```
- 위의 명령어를 실행하고, 정상적으로 동작한다면 `http://localhost:9393/dashboard/#/apps`으로 접속 해 준다


## TODO
- 여러가지 화면들이 보이는데, 하나씩 사용해보려고한다
- 공식문서에 stream, batch 개발자를 위한 여러가지 자습서가있다
    - [stream developer](https://dataflow.spring.io/docs/stream-developer-guides/)
    - [batch developer](https://dataflow.spring.io/docs/batch-developer-guides/)
- 여러가지 예제들도 있는 것 같다
    - [python stream processor](https://dataflow.spring.io/docs/recipes/polyglot/processor/)
    - [amazon kinesis stream processor](https://dataflow.spring.io/docs/recipes/kinesis/simple-producer-consumer/)
    - [Apache Kafka](https://dataflow.spring.io/docs/recipes/kafka/ext-kafka-cluster-cf/)
    