import random
from collections import defaultdict

class Customer:
    
    def __init__(self, name):

        
        self.name = name
        self.order_history = []
        self.topping_chain = defaultdict(lambda: defaultdict(float))
        self.crust_options = ['thin', 'thick', 'stuffed']
        self.cheese_options = ['mozzarella', 'chedar', 'parmesan']
        self.toppings = ['pepperoni', 'mushroom', 'onion', 'olive', 'pineapple', 'sausage', 'bacon', 'anchovy', 'spinach']
        
        for topping in self.toppings:
            for next_topping in self.toppings:
                self.topping_chain[topping][next_topping] = 1 / len(self.toppings)
        
    def generate_order(self):
        """
        Generates a random customer order of pizza (crust, cheese, toppings, cooktime) and then updates the possibility of next topping. 
        
        Args: None
        
        Returns:
            self.order (dict): a dictionary that represents the customer's order. 
                'name' (str):  name of customer
                'crust' (str): crust of the pizza
                'cheese' (str): cheese of the pizza
                'toppings' (list): list of toppings for the pizza
                'cook_time' (float): the cook time for the pizza in minutes
        
        Side Effects:
            Updates self.history by appending generated orders
            Modifies self.topping_chain to update possibility of topping pairs based on previous generated orders
        
        Raises:
            None
        
        """  
        crust = random.choice(self.crust_options)
        cheese = random.choice(self.cheese_options)
        selected_toppings = []
        num_toppings = random.randint(2, 5)
        current_topping = random.choice(self.toppings)
                
        for i in range(num_toppings):
            selected_toppings.append(current_topping)
            next_topping = random.choices(
                self.toppings,
                weights = [self.topping_chain[current_topping][t] for t in self.toppings])[0]
            current_topping = next_topping
                
        for i in range(len(selected_toppings) - 1):
            current = selected_toppings[i]
            next_item = selected_toppings[i + 1]
            self.topping_chain[current][next_item] += 1
                
        for topping, transitions in self.topping_chain.items():
            total = sum(transitions.values())
            for next_topping in transitions:
                transitions[next_topping] /= total
                
        cook_time = 8
        cook_time += 2 if crust == 'stuffed' else 1 if crust == 'thick' else 0
        cook_time += len(selected_toppings) * 0.6
        cook_time = round(cook_time, 2)
                
        order = {
                'name': self.name,
                'crust': crust,
                'cheese': cheese,
                'toppings': selected_toppings,
                'cook_time': cook_time
                }
        self.order_history.append(order)
        return order
        
        
customer = Customer('Daniel')
customer.generate_order()