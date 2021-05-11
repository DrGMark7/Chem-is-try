

A = str(input("Enter Element 1: "))
AA = str(input("Enter Element 2: "))
B = [2,5]
F = [2,9]
Na = [3,11]
Mg = [3,12]
if A[0] != AA[0]:
    print('')
    if A[1] > AA[1]:
        print(f'{A} Bigger than {AA}')
    elif AA[1] > A[1]:
        print(f'{AA} Bigger than {A}')
    else:
        print('Error')

if A[0] == AA[0]:
    print('')
    if A[1] < AA[1]:
        print(f'{A} Bigger than {AA}')
    elif AA[1] < A[1]:
        print(f'{AA} Bigger than {A}')
    else:
        print('Error')
