class Parent:
      def input(self):
          print("ini parent")

class Child(Parent):
    def input(self):
        super().input()
        print("In Child")

c1 = Child()
c1.input()



