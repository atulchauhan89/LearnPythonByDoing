elements=[2,5,10,15,10,2,8,6]
def remove(duplicate):
    num=[]
    for numb in duplicate:
        if numb not in num:
            num.append(numb)
    return  num
print(remove(elements))
