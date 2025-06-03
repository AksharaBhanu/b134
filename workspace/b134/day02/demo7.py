class A:
    def __init__(self):
        self.url='www.fb.com'

    @property
    def title(self):
        return "fb"





obj=A()
print(obj.url) #instance/object variable ,attribute data memeber
# print(obj.title()) #instance/object method, behaviour member function
print(obj.title) #property--> instance method which does not take any arg, must return a value
