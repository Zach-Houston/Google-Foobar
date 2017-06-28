def answer(M, F):
    M2 = int(M)
    F2 = int(F)
    counter = 0
    while True:
        if F2 == 1 and M2 == 1:
            return str(counter)
        elif (F2 < 1 or M2 < 1) or (F2 == M2):
            return "impossible"
        if M2 > F2:
            divisor = M2/F2
            if F2 == 1:
                while M2 != 1:
                    M2 -= 1
                    counter+=1
                continue
            counter += divisor
            M2 -= divisor*F2
        if F2 == 1 and M2 == 1:
            return str(counter)
        elif (F2 < 1 or M2 < 1) or (F2 == M2):
            return "impossible"
        if F2 > M2:
            divisor = F2/M2
            if M2 == 1:
                while F2 != 1:
                    F2 -= 1
                    counter+=1
                continue
            counter += divisor
            F2 -= divisor*M2
