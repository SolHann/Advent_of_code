
def p1(input):
    sum = 0
    
    for x in input:
        combo = ''
        digits = [char for char in x if char.isdigit()]
        combo += digits[0] + digits[-1]
        sum += int(combo)
        
    return sum

def p2(input):
    sum = 0
    for x in input:
        first_digit = ''
        second_digit = first_digit
        combo = ''
        print(x)

        finished = False
        for i in range(len(x)):
            substring = x[:i+1]
            for j in substring:
                if j.isdigit():
                    first_digit = j
                    finished = True
                    break
            for digit, word in enumerate(["zero", "one", "two", "three", "four","five","six","seven","eight","nine"]):
                digit = str(digit)
                if word in substring:
                    first_digit = digit
                    finished = True
            if finished:
                break

            #print(substring)

        finished = False
        for h in range(len(x)):
            substring = x[-h-1:]
            for j in substring:
                if j.isdigit():
                    second_digit = j
                    finished = True
                    break
            for digit, word in enumerate(["zero", "one", "two", "three", "four","five","six","seven","eight","nine"]):
                digit = str(digit)
                if word in substring:
                    second_digit = digit
                    finished = True
            if finished:
                break

        combo = first_digit + second_digit
        print( combo, '\n')
        sum += int(combo)
        
    return sum

with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    #print(p1(items))
    print(p2(items))
    
    # asdfasdfoneight


    #jzln78l6phtndcgseven, 53862