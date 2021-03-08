#inheritance 
class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I am a teacher")


class Customer(User):
    def log(self):
        print("I am a customer")

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    @property
    def name(self):
        #print("getting name")
        return self._name

    @name.setter
    def name(self,name):
        #print("setting name")
        self._name = name

    @name.deleter
    def name(self):
        del self._name
        
    def update_membership(self, new_membership):
        self.membership_type = new_membership
    
    def __str__(self):
        return self.name+" has a "+self.membership_type+" membership"
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self,other):
        if self.name ==  other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None
    __repr__ = __str__

users = [Customer("Agnik","Gold"),
                Customer("Tushar","Bronze"),
                Teacher()]

# print(customers)

# customers[0].log()
for user in users:
    user.log()