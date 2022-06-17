# Apache Spark 사용기
- data 폴더는 데이터들을 담기 위해서 사용하려고한다.
- 데이터 분석에 필요한 데이터는 상대적으로 큰 데이터가 많기때문에 `.gitignore`처리하려고한다


## 목차
[1. Uber Trip Sample with Spark](./example/count_trip/)
    - 아파치 스파크를 활용한 뉴욕 정부에서 제공한 우버트립데이터를 간단히 분석
    - 간단한 샘플코드로 스파크를 실행 할 수 있게 코드생성



## 개발환경
- MacOS M1
- Python 3.9 (Conda)
- Java 1.8
- PySpark 3.2.1

## 환경 설청 및 설치
- 개발환경 세팅하기
    - java 설치
        ```shell
        brew install --cask adoptopenjdk8
        ```
    - scala 설치
        ```shell
        brew install scala
        ```
    - apahce-spark 설치
        ```shell
        brew install apache-spark
        ```
    - python 설치
        ```shell
        brew install python
        ```
        - 혹은, [아나콘다](https://www.anaconda.com/products/distribution)에서 설치해도 된다
    - pySpark 설치
        ```shell
        pip install pyspark
        ```
        - pySpark 실행 확인하기
            ```shell
            pyspark
            ```
    - parquet 데이터 dependency 설치
        ```shell
        pip install pyarrow fastparquet
        ```
    - 데이터 가져오기
        - 미국에서 제공하는 trip data
        ```
        https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
        ```

