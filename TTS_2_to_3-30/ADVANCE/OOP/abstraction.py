# Abstraction

# A Process to hide irrelevant data from the end user

from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def interest(self):
        pass

class SBI(RBI):
    def interest(self):
        print("SBI takes 10% interest on Home Loan")

class HDFC(RBI):
    def interest(self):
        print("HDFC takes 15% interest on Home Loan")

class AXIX(RBI):
    def interest(self):
        print("AXIX takes 17% interest on Home Loan")

#  r1=RBI()
# will give error that instance of abstract class can not be created

s1=SBI()
h1=HDFC()
a1=AXIX()

s1.interest()
h1.interest()
a1.interest()
