# Open-Source-Project-03
오픈소스기초프로젝트 03팀 (아하!)   

get_schedule
-------------
* 학생의 과목을 입력받은 후 엑셀 내 일치하는 데이터를 찾아 리스트에 저장함
  * 학생의 수강과목 시간표
  * 수업시간에 따른 줌 자동 연결 (블랙보드에 줌 링크가 올라오는 경우에만 해당) >> link_to_zoom.py
* CIEAT에서 학생의 전공, 부전공, 복수전공 정보를 가져옴
  * 해당 운영 부서에서 주최하는 비교과 활동 정보를 가져옴 >> enrollment_in_CIEAT   
   
enrollment_in_CIEAT
-------------------
* 사용자의 전공/부전공/복수전공을 토대로 CIEAT의 비교과 활동 정보를 가져옴
  * 운영 부서에 전공과 관련된 문구가 있으면 그것을 채택하는 방식
* 사용자에게 입력받은 운영 부서/키워드를 토대로 CIEAT의 비교과 활동 정보를 가져올 수 있음
* 사용자에게 입력받은 문구가 활동명에 포함된 비교과 활동에 한해서 해당 활동을 자동 신청할 수 있음

link_to_zoom
------------
* 줌은 Chrome이 아닌 외부 어플리케이션이라서 웹 크롤러로 줌 자체를 켤 수 없음
  * 해당 줌 링크의 창을 열도록 함
* 실제로 테스트 해볼 것
