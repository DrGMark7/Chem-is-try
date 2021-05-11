from mendeleev import *


def AtomicRadius_Comparison(Ele_I,Ele_II):

    FirstEle = (element(Ele_I)).atomic_radius
    SecondEle = (element(Ele_II)).atomic_radius

    if  FirstEle > SecondEle :
        Result = f'Element {Ele_I} is larger than {Ele_II}'
        Arrow_Pic =  'Arrow_Right.PNG'
        print(Result)
    elif SecondEle > FirstEle :
        Result = f'Element {Ele_II} is larger than {Ele_I}'
        Arrow_Pic =  'Arrow_Left.PNG'
        print(Result)
    elif SecondEle == FirstEle:
        Result = f'Element {Ele_II} is Equal than {Ele_I}'
        Arrow_Pic = 'Equal_icon.jpg'
    else:
        print('Error')

    ElementPic_I = str(element(Ele_I).atomic_number)+'.PNG'
    ElementPic_II = str(element(Ele_II).atomic_number)+'.PNG'

    Picture_List = [ElementPic_I,ElementPic_II,Arrow_Pic]

    return(Picture_List)