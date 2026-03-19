class employee:
    #special method/ magic method/ dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    
    def travel(self, destination):
        print(f"employee is now travelling to {destination}")

#creating an object/instance of the class
sam = employee()

#printing the attributes
#print(sam.id)

#calling method
#sam.travel("kerala")

print(type(sam))