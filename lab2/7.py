import json
import random
from Zadacha_5 import print_result
from Zadacha_6 import cm_timer_1


path = "/Users/acti0n/Documents/proga/lab2/data.json"   

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(set(item['job-name'].lower() for item in arg))

@print_result
def f2(arg):
    return list(filter(lambda s: s.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda s: s + ' с опытом Python', arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 2000000) for _ in range(len(arg))] 
    return ['{} зарплата {}'.format(job, salary) for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

