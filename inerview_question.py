class interview(object):
    #Write a function that prints the numbers from 1 to 100.

    def question_1(self):
        number = range(1,100)
        for i in number:
            if i % 3 == 0:
                print 'Foo'
            elif i % 5 ==0:
                print 'FooBar'
            else:
                print i
        return

