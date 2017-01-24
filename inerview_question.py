
    #Write a function that prints the numbers from 1 to 100.

def question_1():
        number = range(1,100)
        for i in number:
            if i % 3 == 0:
                print 'Foo'
            elif i % 5 ==0:
                print 'FooBar'
            else:
                print i
        return

def question_2(int):
    temp = 0
    for i in range(0,int+1):
        if i % 2 == 0:
            temp +=1
    print temp
    return

def question_3():

    return

print question_1()