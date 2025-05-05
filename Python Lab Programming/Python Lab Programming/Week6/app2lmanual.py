class ClassA:
    def m(self):
        print("In ClassA")

class ClassB(ClassA):
    def m(self):
        print("In ClassB")

class ClassC(ClassA):
    def m(self):
        print("In ClassC")

class ClassD(ClassB, ClassC):
    def m(self):
        print("In ClassD")

# Create an object of ClassD
obj = ClassD()

# Call the method from the object
obj.m()

# Check the MRO (Method Resolution Order) of ClassD
print("\nMRO of ClassD:", ClassD.__mro__)


