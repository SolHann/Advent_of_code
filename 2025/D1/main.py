def p1(input):
    count = 0
    dial = 50
    for x in input:
        turn = int(x[1:])
        if x[0] == 'R':
            dial += turn
        else:
            dial -= turn
        dial = dial % 100
        
        if dial == 0:
            count += 1

    return count

def p2(input):
    count = 0
    dial = 50  
    dial_prev = 50
    
    for x in input:
        dial = dial % 100
        dial_prev = dial
        turn = int(x[1:])

        if x[0] == 'R': 
            dial += turn
            if dial >= 100:
                count += dial // 100
            if dial % 100 == 0: 
                count -= 1 
        else:
            dial -= turn
            if dial < 0 and dial_prev != 0 :
                count += abs(dial // 100)
            elif dial < -100 :
                count += abs(dial // 100) - 1        
        if dial == 0:
            count += 1

    return count

with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items)) 