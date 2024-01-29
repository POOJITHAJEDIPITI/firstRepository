import time
def duration(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(f'the total time taken to answer the question is{end-start}sec')
    return inner
@duration
def question1():
    print('who is mother theresa institute chairman')
    response=input('')
def question2():
    print('who is Indian financial minister')
    response=input('')
#question1()
#question2()
