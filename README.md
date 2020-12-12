# Python Click 라이브러리 예제 모음

click 공식 사이트
- https://click.palletsprojects.com/en/7.x/


## 자동완성 기능 추가하기
1. setuptools 를 사용해야 한다.(setup.py 설정)
2. `_CLI_COMPLETE=source_bash cli > cli-complete.sh` 명령을 사용해 bash_completion 스크립트를 생성하고 이것을 ~/.bashrc에 삽입한다.
3. 파일 수정시마다 `python setup.py install` 명령을 수행해 변경사항을 반영한다.


## 유닛 테스트 추가하기
1. pytest install 및 테스트 파일 작성
2. 테스트 수행하기 `pytest -s `
