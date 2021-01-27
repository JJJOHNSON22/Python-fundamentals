import random
def randInt(max_num=0, min_num=0):
    if (min_num==0 and max_num==0 or min_num > max_num or max_num < 0):
        if (max_num < min_num):
            num = int(random.uniform(max_num, min_num))
            return num
        else:
            num = int(random.random() * 100)
            return num
    elif (min_num!=0 and max_num!=0):
        num = int(random.random() * max_num + min_num)
        return num
    elif (max_num!=0):
        num = int(random.random() * max_num)
        return num
    else:
        num = int(random.random() * 100 + min_num)
        return num

print(randInt())
print(randInt(max_num=-30))
print(randInt(max_num=47))
print(randInt(min_num=23))
print(randInt(min_num=20, max_num=522))
print(randInt(min_num=240, max_num=-58))
