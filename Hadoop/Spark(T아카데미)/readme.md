## Apache Hadoop의 구성요소

- HDFS (분산 파일 시스템)
- Yarn (Resource Manager)
- MapReduce, Spark
- Hive, Impala
- Zookeeper (Monitor)

## HDFS

- GFS 논문에서 시작
- Hadoop Distributed File System
- Reliability 제공 (장애 복구)
- Master-Slave 디자인  

## HDFS의 구성

- Master Node: metadata, 위치 정보 관리
- Slave Nodes: 실제 데이터 저장

## HDFS Block

- 파일의 Block의 복제(3카피)를 여러 노드에 분산하여 저장하여 장애에 대비
- 파일을 64MB 혹은 128MB 단위로 분리하여 저장

## Apache Spark

- 기존의 MapReduce보다 더 빠르게 컴퓨팅한다. 
- 컴퓨터 클러스터에서 병렬 프로세싱을 위한 라이브러리 집합, 통합된 컴퓨팅 엔진
- Cluster Manager 
    - Driver
    - Executors

