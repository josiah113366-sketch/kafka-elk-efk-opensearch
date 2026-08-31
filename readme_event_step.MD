# 목표
- 기존 로그젠 -> fluent-bit -> kafka -> vector -> firehose 동일 
  - kafka를 굳이 사용하는 이유? 
    - 데이터 트래픽이 급상승, 처리량 많아질 때 
      - 안정성 제공 (손실 x) 
      - 극저지연 전송
      - 토픽을 구독하는 여러 컨슈머에게 동시 전송 가능함
        - 원소스 멀티 유즈 사용 가능
      - ... 
- firehose -> s3 bronze 적재 
            -> EventBridge 서비스 
              -> 이벤트 버스 + (스케줄)
                - `이벤트` 트리거 활용 메달리온 아키텍처 기반 전처리 수행
                - Airflow에서는 센서를 이용하여 이벤트 감지 -> task 작동
              -> [v] 스케줄 
                - 특정 시간이 되면 (매시간 10분에 `스케줄링`) 메달리온 아키텍처 기반 전처리 수행
                - Airflow에서 스케줄 적용 task 작동
            -> 트리거 작동 -> 실제 작업(task) 진행 : Step Functions
              -> 메달리온 아키텍처 기반 전처리 수행 실제 세부 task를 구성 -> ... -> s3 하위에 silver, gold, 기타 등등 데이터들을 처리하여 세팅해둠 -> 대시보드, 각종 서비스에서 s3를 조회하여(athena, ...)를 활용
            -> glue 등에서 db/table 등, job(전처리-pandas, polars, pyspark)을 구성 진행 -> task에 관여, 저장 형태(컬럼)

- 요약 
  - 배치 프로세싱 기준, 저비용, 고효율 작업 구성
    - EventBridge : 트리거 역할/본 프로젝트는 스케줄만 적용 
    - Step Functions : 실제 절차적 task 담당. ETL 수행, 메달리온 아키텍처 처리 task 정의 
    - glue : 데이터 구조에 따른 스키마, ETL JOB을 제공(스파크, pandas 활용)
    - 기타 : 권한, 변수 등 조정, 추가
    - firehose에서 기존 opensearch(제거)로 가는 방향성, s3로 변경

# 인프라 구성
```
eventbridge.tf
stepfunctions.tf
glue.tf
catalog.tf
athena.tf
iam-xxx.tf
...
```