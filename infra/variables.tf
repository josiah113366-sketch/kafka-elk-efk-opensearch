variable "aws_region" {
  description = "AWS 리전"
  type        = string
  default     = "ap-northeast-2"
}

variable "project_name" {
  description = "프로젝트명"
  type        = string
  default     = "de-ai-16-kafka-efk"
}

# opensearch 서비스(<- 엘라스틱서치)/ opensearch 대시보드(<- 키바나) 접속 가능한 IP 입력
variable "allowed_cidr" {
  description = "opensearch 대시보드/API에 접속한 공인 IP x.x.x.x/32"
  type        = string
  default     = "222.108.125.33/32"
  # 접속 위치가 바뀌면 접근 x -> ip를 변경하여 인프라 반영시켜야 함 
  validation {
    condition     = can(cidrhost(var.allowed_cidr, 0))
    error_message = "가능한 주소는 CIDR 형식이어야 합니다."
  }
}

# opensearch, spec(버전, 인스턴스 유형, 볼륨 단위, 인덱스 등 설정)
variable "opensearch_index_name" {
  description = "firehose가 데이터를 opensearch에 적재할 때 세팅하는 인덱스 값"
  type        = string
  default     = "factory-sensor-001"
}

variable "firehose_buffer_size" {
  description = "오픈 서치로 전송할 때 최대 버퍼 사이즈"
  type        = number
  default     = 1
}
variable "firehose_buffer_interval" {
  description = "오픈 서치로 전송할 때 최대 버퍼 시간(s)"
  type        = number
  default     = 60
}

# firehose 이름, firehose -> opensearch : iam role name

# vector -> firehose : iam role name