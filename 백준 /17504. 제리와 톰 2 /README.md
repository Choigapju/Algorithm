분수 구현 문제는 코드로 작성을 할 때 뇌 주름을 너무 많이 사용해서 큰일이다. 더 익숙해져 구현이 수월할 수 있도록 연습을 해야 할거 같다.

어떻게 풀어야 할진 알겠으나, 분수 계산을 어떻게 해야 할지 빠르게 떠오르지가 않아 구글링을 좀 하여 다른 풀이자들의 답변을 참고 하였다.

N개만큼 입력된 a_n에 대해서, 역수를 취한 다음, 우리가 해줘야 할 계산을 천천히 해주는데, 1/(a/b)꼴이 되기때문에 풀이를 해주면 b/a로 역수 계산이 이루어진다. 이를 단순히 a, b = b, a로 구현을 하였던데, 코드를 이렇게 작성해야겠다는 느낌이 오질 않아 풀이를 못 하고 있었다

최초의 분수 풀이가 a_n-1 + 1/(a_n)이기 때문에 a, b = 1, 1로 초기값 설정을 해주는데, 이후 계산을 하면서 분모에는 계속 1이 입력될 것이기 때문에 반복 바깥에 지정을 해준다.

그리고 앞서 말 했든 최초의 계산은 1/a_n이기에 if i == 0: b = A[0]으로 설정한 뒤 다음 i 값으로 넘어가도록 continue를 시행 해 준다.

그 다음부터는 분수의 분모값 계산을 차근히 진행하여 주는데, A = [2, 7, 1, 8]이라 가정 했을 때, 역수 변환을 해주었기에 A = [8, 1, 7, 2]가 된다.
따라서, 1+1/8이 되는데 9/8을 표현하기 위해 (그 다음 인덱스로 넘어가면 1/(9/8)= 8/9가 되기에) a = A[i] * b + a를 수행한 뒤, 위에서 말한 역수 계산을 진행해 주기 위해 a, b = b, a를 시행 한다.

그렇게 반복하여 나온 값에서 b-a: 분자, b: 분모를 print하여 결과를 출력한다.

.
.
.

분수 계산은 구현이 머리랑 손이랑 따로 노는 기분이라 많은 연습으로 체득이 필요 한 것 같다 ᴗ_ᴗ̩
