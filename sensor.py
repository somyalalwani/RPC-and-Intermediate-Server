import schedule
import time
import random

def s1():
    with open("1.txt","a+") as f1:
        info=str(random.randint(5,20))
        f1.write(info)
#to generate random data for sensor 1

def s2():
    with open("2.txt","a+") as f2:
        info=str(random.randint(10,20))
        f2.write(info)

#to generate random data for sensor 2


schedule.every(2).seconds.do(s2)
schedule.every(4).seconds.do(s1)

while True:
    schedule.run_pending()
