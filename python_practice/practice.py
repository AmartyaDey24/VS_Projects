class A:
    def fun(self):
        print('A')

class B:
    def fun(self):
        print('B')

class C(B,A):
    def fun1(self):
        super().fun()
        #print('C')

c = C()
c.fun1()



