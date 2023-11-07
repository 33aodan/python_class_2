class A:
    def jit1(self):
        print("blud tripping")
class B(A):
    def jit2(self):
        print("pronouns are nick/her")

class C(B):
    def jit3(self):
        print("konichiwa, ogenkidesuka?? i am sugoii!")
        super().jit1()
        super().jit2()


obj=C()
obj.jit3()
