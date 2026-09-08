class Math:
    def __init__(self,num):
        self.num=num

    def subfromnum(self,num1):
        self.num=self.num-num1

    # def add(self,num1,num2):
    #     print("Hello bhai")
    #     return num1+num2
        
    # static method is called whenever we call the mwthod add because it is not dependent on the instance of the class. It can be called using the class name or an instance of the class.
    @staticmethod
    def add(num,num2):
        print("Hello")
        return num+num2
        


a=Math(10)
print(a.num)
a.subfromnum(5)
print(a.num)
print(a.add(10,20))
print(Math.add(20,30))