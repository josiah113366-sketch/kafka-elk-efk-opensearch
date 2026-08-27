# 목표
- kafka 이해, 활용, 응용 
- ELK, EFK에서 
  - 데이터 전송/필터링/전처리 등 역할 담당
  - L : Logstash   -> 라이브러리 활용, 비정형 데이터(text 로그 파일) -> 가공 -> json 전송
  - F : Fluent-Bit -> json 전송, text 전송
  - 센서 장비 + 장비 등(배치 ) -> 로그 발생 -> 바로 전송(Fluent-Bit/Logstash) -> kafka 전송 -> vector -> firehose -> opensearch/s3 -> 검색 서비스 활용
- opensearch
  - E : 엘라스틱 서치의 AWS 버전(저작권 오픈된 버전)
  - 검색 엔진, 인덱스 검색 
  - 대시보드 <-> K : 키바나

# 목표 시스템 