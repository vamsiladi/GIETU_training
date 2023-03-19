class vechile:
    def __init___(s):
        s.__id=None
        s.__type=None
        s.__cost=None
        s.__amount=None
    def premium_amount(s,type):
        if type=='two wheeeler':
            s.__amount=int(s.__cost*0.02)+int(s.__cost)
        elif type=='four wheeler':
            s.__amount=int(s.__cost*0.06)+int(s.__cost)
    def set_id(s,id):
        s.__id=id
    def get_id(s):
        return s.__id
    def set_type(s,type):
        if type == 'two wheeler':
            s.__type=type
        elif type == 'four wheeler':
            
            s.__type=type
        else:
            s.__type='error'
    def get_type(s):
        return s.__type
    def set_cost(s,cost):
        s.__cost=cost
    def get_cost(s):
        return s.__cost
    def get_amount(s):
        return s.__amount
a=vechile()    
id=input()
type=input()
cost=input()
a.set_id(id)
a.set_type(type)
a.set_cost(cost)
print(a.get_cost())
print(a.get_amount())
    
          
        
