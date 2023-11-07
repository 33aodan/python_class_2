class phone:
    def call(self):
        print("You can call")
    def sms(self):
        print("you can text")
class samsung:
    def call(self):
        print("You can call")
    def sms(self):
        print("you can text")
    def photo(self):
        print("You can capture moments")

p=phone()
p.call()
p.sms()

sam=samsung()
sam.call()
sam.sms()
sam.photo()