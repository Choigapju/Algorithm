def solution(survey, choices):
    answer = ""
    mbti = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        if choices[i] > 4:
            mbti[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            mbti[survey[i][0]] += 4 - choices[i]
            
    if mbti["R"] >= mbti["T"]:
        answer += 'R'
    else:
        answer += 'T'
        
    if mbti["C"] >= mbti["F"]:
        answer += 'C'
    else:
        answer += 'F'
        
    if mbti["J"] >= mbti["M"]:
        answer += 'J'
    else:
        answer += 'M'
    
    if mbti["A"] >= mbti["N"]:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer
