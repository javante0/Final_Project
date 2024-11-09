import random

class Customer:
    def __init__(self, name, allergies=None):
        
        self.name = name
        self.allergies = allergies if allergies else []
        self.order = None
        
    def generate_order(self):
        crust_options = ['thin', 'thick', 'stuffed']
        cheese_options = ['mozzarella', 'chedar']
        sauce_options = ['tomato', 'white', 'spicy', 'pesto']
        topping_options = ['pepperoni', 'mushroom', 'onion', 'sasuage', 'pineapple', 'green pepper', 'canadian bacon', 'olive']
        slice_options = [4, 6, 8, 12]
        size_options = ['small', 'medium', 'large']
        
        toppings = [topping for topping in topping_options if topping not in self.allergies]
        
        crust = random.choice(crust_options)
        cheese = random.choice(cheese_options)
        sauce = random.choice(sauce_options)
        size = random.choice(size_options)
        topping_amount = random.randint(1, 5)
        chosen_toppings = random.sample(toppings, min(len(toppings), topping_amount))
        slices = random.choice(slice_options)
        
        original_time = {'small': 8, 'medium': 10, 'large': 12}
        cook_time = original_time[size]
        
        crust_cooking_adjustments = {
            'thin': -1,
            'thick': 2,
            'stuffed': 3
        }
        
        cook_time += crust_cooking_adjustments.get(crust, 0)
        cook_time += len(chosen_toppings) * 0.3
        cook_time += round(cook_time, 2)
        
        self.order = {
            'name': self.name,
            'crust': crust,
            'sauce': sauce,
            'cheese': cheese,
            'toppings': chosen_toppings,
            'slices': slices,
            'cook time': cook_time
        }
        return self.order
        
customer = Customer('Daniel')
customer.generate_order()
        