# Spark Package 가져오기
from pyspark import SparkConf, SparkContext

# Pandas 패키지 가져오기
import pandas as pd

# 스파크 설정하기
conf = SparkConf().setMaster("local").setAppName("My First Test App")
sc = SparkContext(conf=conf)

# 데이터 디렉토리
direct = "/Users/wool/Develop/Github/data-flow-framework/apache-spark-starter/data"
filename = "trip_data.csv"

# data parse
lines = sc.textFile(f"file:///{direct}/{filename}")
header = lines.first()
filtered_lines = lines.filter(lambda row: row != header)

# 필요한 부분 추출
dates = filtered_lines.map(lambda x: x.split(",")[4].split(" ")[0])
result = dates.countByValue()

# csv로 결과값 저장
pd.Series(result, name="trips").to_csv(f"{direct}/result_data/result_trips_data.csv")
