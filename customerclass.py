import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []
        self.probability_chain = {}
        self.crust_options = ['thin', 'thick', 'stuffed']
        self.cheese_options = ['mozzarella', 'cheddar', 'parmesan']
        self.toppings = ['pepperoni', 'mushroom', 'onion', 'olive', 'pineapple', 'sausage', 'bacon', 'anchovy', 'spinach']
        self.size = ['small', 'medium', 'large']
        for topping in self.toppings:
            self.probability_chain[topping] = {}
            for next_topping in self.toppings:
                self.probability_chain[topping][next_topping] = 1 / len(self.toppings)

    def generate_order(self):
        """
        Generates a random customer order of pizza (crust, cheese, toppings, cooktime) and then updates the possibility of next topping. 
        
        Args: None
        
        Returns:
            str: The first value in the order dictionary when we iterate over the values. Utilizes fstrings in order to incorporate specific parts of the order in the returned strings
            
        
        Side Effects:
            Updates self.history by appending generated orders
            Modifies self.probability_chain to update possibility of topping pairs based on previous generated orders
        
        Raises:
            None
        """  
        crust_type = random.choice(self.crust_options)
        cheese_type = random.choice(self.cheese_options)
        selected_toppings = []
        num_toppings = random.randint(2, 5)
        first_topping = random.choice(self.toppings)
        size = random.choice(self.size)
                
        for topping in range(num_toppings):
            selected_toppings.append(first_topping)
            next_topping = random.choices(
                self.toppings,
                weights = [self.probability_chain[first_topping][t] for t in self.toppings])[0]
            first_topping = next_topping
                
        for topping in range(len(selected_toppings) - 1):
            current = selected_toppings[topping]
            next_item = selected_toppings[topping + 1]
            if next_item not in self.probability_chain[current]:
                self.probability_chain[current][next_item] = 0
            self.probability_chain[current][next_item] += 1
                
        for topping, transitions in self.probability_chain.items():
            total = sum(transitions.values())
            for next_topping in transitions:
                transitions[next_topping] /= total
                
        cook_time = 6
        cook_time += 1.5 if crust_type == 'stuffed' else 1 if crust_type == 'thick' else 0
        cook_time += len(selected_toppings) * 0.6
        cook_time = round(cook_time, 1)

        order = {
                'separator1': "---------------------------------",
                'name': f"{self.name}'s ORDER",
                'separator2': "---------------------------------",
                'size': f"{size}",
                'crust': f"{crust_type} crust",
                'cheese': f"{cheese_type} cheese",
                'toppings': f"Ingredients: {selected_toppings}",
                'cook_time': f"Cook for {cook_time} minutes",
                'separator3': "---------------------------------"
                }
        self.order_history.append(order)
        for step in order.values():
            print(step)
        
        
customer = Customer('Daniel')
customer.generate_order()
