class OverloadDemo:
    # sum method with one default parameter
    def sum(self, a, b, c=0):
            s = a + b + c
            return s

od =  OverloadDemo()
#calling method with 2 args
sum = od.sum(7, 8)
print('sum is-', sum)
#calling method with 3 args
sum = od.sum(7, 8, 9)
print('sum is-', sum)