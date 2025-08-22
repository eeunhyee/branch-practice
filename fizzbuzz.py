for j in range(1, 45+1):
    if j % 3 == 0:
        if j % 5 == 0:
            print('fizzbuzz')
        print('fizz')
    elif j % 5 == 0:
        if j % 3 == 0:
            print('fizzbuzz')
        print('buzz')
    else:
        print(j)
