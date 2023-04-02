a = int(input())
b = int(input())
if a > b:
    if a // b >= 3:
        print('Больше чем в три раза')
    else:
        print('Больше')
else:
    print('Меньше')
