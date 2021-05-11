from mendeleev import *

def IE_EN_Comparison(Ele_IE_I , Ele_IE_II):

    FirstEle = (element(Ele_IE_I)).ionenergies[1]
    SecondEle = (element(Ele_IE_II)).ionenergies[1]

    if  FirstEle > SecondEle :
        Result = f'Element {Ele_IE_I} has a higher energy than {Ele_IE_II}' 
        print(Result)
    elif SecondEle > FirstEle :
        Result = f'Element {Ele_IE_II} has a higher energy than {Ele_IE_I}'
        print(Result)
    else:
        print('Error')

    return(Result)
