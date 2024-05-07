#implementing stack using inheriting list class
from prac import * 

class Stack(Sll):
    def is_empty(self):
        return super().isEmpty()   #by using super() we can call function of SLL or any other inherited class
     