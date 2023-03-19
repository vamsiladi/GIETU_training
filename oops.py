class student:
    def __init__(self,id,age,marks,fees):
        self.__id=id
        self.__age=age
        self.__marks=marks
        self.__fees=fees
    def validate_marks(self):
        if 0<=self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
         if self.validate_marks() and self.validate_age():
             if self.__marks>65:
                 return True
             else:
                 return False
    def discount(self):
        if self.check_qualification() and self.__marks>85:
            print(self.__fees*0.25)
        else:
            print(self.__fees)
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

    def get_fees(self):
        return self.__fees



s=student(101,22,88,1000)

print(s.check_qualification())
s.discount()


    
        
