# __init___.py 파일 (패키지 초기화 파일)
# 패키지를 로드할 때 실행되는 초기화 파일

# 1. 패키지를 import할 때 실행되어야 하는 초기화 코드 작성(환경 확인(예를 들어 의존성 패키지 버전 체크))
# 2. 패키지 메타데이터 작성(버전, 작성자)
# 3. 패키지 re-import
#   만일 패키지 아래 디렉토리가 여러 개 존재하면, from mypackage.(디렉토리명/mymath) import add처럼 써야 하는데, 이러한 패키지 구조를 몰라도 쉽게 쓸 수 있도록 하는 것이 패키지 re-import다.

print("__init__")

# 2. 패키지 메타데이터 작성(버전, 작성자)
VERSION = "1.0.0"

# 3. 패키지 re-import
from mypackage.mymath import add # 절대 경로로 import : 패키지명이 바뀌면 전부 바꿔야 해서 좋지 않음.
from .mymath import add # 상대 경로로 import : 패키지명을 안 쓰고, 현재 위치를 기준으로 import하도록 함.