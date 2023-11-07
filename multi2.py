class A:
    def somethingfun(self):
        print("badminton")
class B:
    def somethingfun(self):
        print("coding")
class C(B, A):
    def somethingfun(self):
        print("using the toilet")
        super().somethingfun()
        super().somethingfun()
obj=C()
obj.somethingfun()