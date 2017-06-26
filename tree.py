
def findVal(val, num, height):
    left = num - (2**(height-1))
    right = num - 1
    if val == left or val == right:
        return num
    if val < left:
        return findVal(val, left, height-1)
    else:
        return findVal(val, right, height-1)

def answer(h, q):
    answers = []
    for val in q:
        if val == (2**h)-1:
            answers.append(-1)
            continue
        answers.append(findVal(val, (2**h)-1, h))
    return answers

