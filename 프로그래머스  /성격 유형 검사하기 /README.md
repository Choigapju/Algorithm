###
* dict 형식으로 (성격 유형 검사라서) mbti라는 변수로 1번 지표부터 4번 지표까지의 결정 유형을 0으로 초기화 하여 입력.

* for문으로 len(survey)로 인덱스 번호로써 변수 i로 길이를 순회, 이 때 choices[i]가 4보다 크다면 <br>mbti[survey[i][1]에 choices[i]-4 만큼 합하여 주고, 4보다 작으면 4-choices[i]만큼을 더하여 준다.

제1 지표부터 4 지표까지 각각을 살피면서, "단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다."의 조건에 따라<br>각 유형의 먼저 나온 글자에 입력된 값이 더 크면 해당 유형을 answer에 더해주어 결과를 도출한다. 
