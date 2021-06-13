



What do data engineers focus on?

Data engineers primarily focus on the following areas.

## Build and maintain the organization’s data pipeline systems

## Clean and wrangle data into a usable state


They need to know Linux and they should be comfortable using the command line.
They should have experience programming in at least Python or Scala/Java.
They need to know SQL.
They need some understanding of distributed systems in general and how they are different from traditional storage and processing systems.
They need a deep understanding of the ecosystem, including ingestion (e.g. Kafka, Kinesis), processing frameworks (e.g. Spark, Flink) and storage engines (e.g. S3, HDFS, HBase, Kudu). They should know the strengths and weaknesses of each tool and what it’s best used for.
They need to know how to access and process data.

## 주요 업무

수집, 가공, 저장
수많은 서비스에서 생산된 수많은 데이터를 모을 수 있도록 거대한 데이터 파이프라인을 설계, 구축합니다. 모두가 쉽고 안전하게 다룰 수 있도록 가공 처리를 하며, 데이터의 성격에 따라 스트리밍 혹은 배치 처리를 합니다. 이것을 제대로 하려면 적합한 기술들의 선택과 조화로운 설계가 필요합니다. 그래서 쉬운 일이 아니고 더 많은 데이터 엔지니어가 필요한 근본적인 이유가 되지요.


분석
저장된 데이터에서 hive 등의 쿼리로 일회성 분석을 하기도 합니다. 그래서 데이터 엔지니어는 쿼리에 대한 이해가 필요합니다. visualization tool 을 통해 self service BI (직원 누구나 접속하여 분석할 수 있는 환경) 환경을 개발하기도 합니다. 데이터에 대한 이해와 시각화 툴에 대한 이해가 동시에 필요하겠죠.


협업
심화된 분석, ML, AI 등을 하는 데이터 사이언티스트들과 협업이 필요합니다. 어떤 데이터들을 쓰고 있고, 어떤 데이터들이 필요한지 알아야 일이 원활하게 진행이 되니까요. 일이 원활하게 진행이 된다면 서비스는 점점 더 사용자가 원하는 콘텐츠를 추천하게 될 것입니다.

## 데이터 파이프라인

- 데이터 분석가 및 사내 다양한 팀들이 손쉽게 서비스 데이터를 다루고 분석할 수 있는 기반을 마련합니다.
- 데이터 분석팀들이 만든 모델 혹은 비즈니스 로직을 실제로 적용할 수 있도록 백엔드 서비스를 개발하고 환경을 구축합니다.
- 데이터 적재의 자동화, 속도와 확장 가능성을 고려한 운영, 그리고 개발과 인프라에 대한 것들이 포함되어 있습니다.

Scalability: 기하급수적으로 늘어났을때도 작동

Stability: 에러, 데이터 플로우 모니터링

Security: 데이터 이동 간 보안 관리

## Data Pipeline

- Real time data pipeline
- Batch data pipeline

## ETL

##


Hadoop, Kafka,






## 참고자료

[1] https://tech.kakao.com/2020/11/30/kakao-data-engineering/

[2] https://www.youtube.com/watch?v=VtzvF17ysbc