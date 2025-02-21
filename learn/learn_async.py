# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")



# x = filter(lambda x: x%2==0, [1,2,3,4,5])
# y = map(lambda x: x*2, [1,2,3,4,5,6])
# print(f"======= {list(x)}")
# print(f"=======22 {list(y)}")
# print(f"=======z {list(y)}")

x = filter(lambda x: x%2==0, [1,2,3,4,5])
y = list(map(lambda x: x*2, [1,2,3,4,5,6]))
print(f"======= {list(x)}")
print(f"=======22 {(y)}")
y.sort(reverse = True)
print(f"=======z {y}")

numbers = [7, 3, 11, 2, 5]

# reverse is set to True
numbers.sort(reverse = True)

print(numbers)

dic = {}
set1 = {1,2}
def func():
    dic['a']=1
    set1.add(3)

func()
print(f'dic is {dic}')
print(f'set is {set1}')

class Student:
    count1 = 1
    def __init__(self, count2=2, count3 = 0):
        self.count2 = count2
        self.count3 = count3 + 1
        self.count1 = self.count1 + 1

        
s=Student()
s.count3=3
print(f'==== {s.count1}, {s.count2}, {s.count3}')

s2=Student(3)
print(f'==== {s2.count1}, {s2.count2}, {s2.count3}')

import time
def task1():
    print("====== task 1")
    time.sleep(1)

def task2():
    print("====== task 2")
    time.sleep(1)

task1()
task2()
print('done')

print("=========Async or Concurrency")

import asyncio
async def task1():
    print("====== task 1")
    await asyncio.sleep(3)
    print("====== done task 1")

async def task2():
    print("====== task 2")
    await asyncio.sleep(2)
    print("====== done task 2")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(task1(), task2())

asyncio.run(main())
print('done async')

print("=========Parallelism")
from multiprocessing import Process

def task(name):
    print(f"Task {name} started")
    # Simulate some CPU-bound work
    sum([i**2 for i in range(1000000)])
    time.sleep(2)
    print(f"Task {name} finished")

# Create and start multiple processes for parallel execution
p1 = Process(target=task, args=("1",))
p2 = Process(target=task, args=("2",))

p1.start()
p2.start()

p1.join()
p2.join()




