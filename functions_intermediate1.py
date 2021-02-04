import random
def randInt(max_num=0, min_num=0):
    if (min_num==0 and max_num==0):
        num = int(random.random() * 100)
        return num
    elif (min_num!=0 and max_num!=0):
        num = int(random.random() * (max_num - min_num) + min_num)
        return num
    elif (max_num!=0):
        num = int(random.random() * max_num)
        return num
    else:
        num = int(random.random() * (100 - min_num) + min_num)
        return num

print(randInt())
print(randInt(max_num=50))
print(randInt(min_num=50))
print(randInt(min_num=50, max_num=500))
