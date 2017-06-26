def answer(xs):
    total = 1
    found = False
    zero = False
    negatives = []
    if len(xs) == 1:
        return str(xs[0])
    for num in xs:
        if num == 0:
            zero = True
            continue
        if num > 0:
            total = total * num
            found = True
        if num < 0:
            found = True
            negatives.append(num)
            
    if (len(negatives) % 2 == 0):
        for n in negatives:
            total *= n
    elif(len(negatives) == 1):
        if zero == True:
            return str(0)
        if total == 1:
            return str(negatives[0])
        return str(total)
    else:
        negatives.sort()
        for n in negatives[:-1]:
            total *= n
    if total == 1 and found == False:
        return str(0)
    if total < 0 and zero == True:
        return str(0)
    return str(total)
