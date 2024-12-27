def solution(survey, choices):
    rt = [0, 0]
    cf = [0, 0]
    jm = [0, 0]
    an = [0, 0]
    answer = []
    
    for index, value in enumerate(survey):
        if value == 'RT':
            if choices[index] < 4:
                rt[0] += 4-choices[index]
            else:
                rt[1] += choices[index]%4
        elif value == 'TR':
            if choices[index] > 4:
                rt[0] += choices[index]%4
            else:
                rt[1] += 4-choices[index]
                
        if value == 'CF':
            if choices[index] < 4:
                cf[0] += 4-choices[index]
            else:
                cf[1] += choices[index]%4
        elif value == 'FC':
            if choices[index] > 4:
                cf[0] += choices[index]%4
            else:
                cf[1] += 4-choices[index]
                
        if value == 'JM':
            if choices[index] < 4:
                jm[0] += 4-choices[index]
            else:
                jm[1] += choices[index]%4
        elif value == 'MJ':
            if choices[index] > 4:
                jm[0] += choices[index]%4
            else:
                jm[1] += 4-choices[index]
                
        if value == 'AN':
            if choices[index] < 4:
                an[0] += 4-choices[index]
            else:
                an[1] += choices[index]%4
        elif value == 'NA':
            if choices[index] > 4:
                an[0] += choices[index]%4
            else:
                an[1] += 4-choices[index]
                
    if rt[0] > rt[1]:
        answer.append('R')
    elif rt[0] == rt[1]:
        answer.append('R')
    else:
        answer.append('T')
        
    if cf[0] > cf[1]:
        answer.append('C')
    elif cf[0] == cf[1]:
        answer.append('C')
    else:
        answer.append('F')
        
    if jm[0] > jm[1]:
        answer.append('J')
    elif jm[0] == jm[1]:
        answer.append('J')
    else:
        answer.append('M')
        
    if an[0] > an[1]:
        answer.append('A')
    elif an[0] == an[1]:
        answer.append('A')
    else:
        answer.append('N')
    
    return ''.join(answer)


def solution(survey, choices):
    scores = {
        'R':0, 'T':0,
        'C':0, 'F':0,
        'J':0, 'M':0,
        'A':0, 'N':0
    }
    
    indicators = [
        ('R', 'T'),
        ('C', 'F'),
        ('J', 'M'),
        ('A', 'N')
    ]
    
    answer = []
    
    for survey, choice in zip(survey, choices):
        first, second = survey
        
        if choice > 4:
            scores[second] += choice-4
        else:
            scores[first] += 4-choice
            
    for first, second in indicators:
        if scores[first] > scores[second]:
            answer.append(first)
        elif scores[first] < scores[second]:
            answer.append(second)
        else:
            answer.append(min(first, second))
        
    return ''.join(answer)