class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary    
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        self.pants_sold.append(pants_object)

    def display_sales(self):
        for pants in self.pants_sold:
            print(f"color: {pants.color}, waist_size: {pants.waist_size}, length: {pants.length}, price: {pants.price} ")

    def calculate_sales(self):
        for i in range(len(self.pants_sold)):
            self.total_sales = self.total_sales + self.pants_sold[i].price
        
        return self.total_sales

    def calculate_commission(self, percentage):
        return self.total_sales*percentage
