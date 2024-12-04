from collections import defaultdict
import time
import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []
        self.probability_chain = {}
        self.crust_options = ['thin', 'thick', 'stuffed']
        self.cheese_options = ['mozzarella', 'cheddar', 'parmesan']
        self.toppings = ['pepperoni', 'mushroom', 'onion', 'olive', 'pineapple', 'sausage', 'bacon', 'anchovy', 'spinach']
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
                'crust': f"{crust_type} crust",
                'cheese': f"{cheese_type} cheese",
                'toppings': f"Ingredients: {selected_toppings}",
                'cook_time': f"Cook for {cook_time} minutes",
                'separator3': "---------------------------------"
                }
        self.order_history.append(order)
        for step in order.values():
            return(step)

customer = Customer('Daniel')
customer.generate_order()

order = {
            'name': "John",
            'crust': "Thick",
            'size': "Large",
            'sauce': "Marinara",
            'cheese': {"Cheddar"},
            'toppings': {"Pepperoni", "Bacon"},
}

def pizza_prep():
    """
    Mechanism that allows takes a customer's order and prompts the user to type the ingredients included
    in the order. The user's score for this portion is calculated based on how quickly they type all
    ingredients and how accurately they type each ingredient.

    Side effects:
    crust_input: prompts the user to type in the order's crust

    size_input: prompts the user to type in the order's size

    sauce_input: prompts the user to type in the order's sauce

    cheese_input: prompts the user to type in the order's cheese/s

    toppings_input: prompts the user to type in the order's topping/s

    Prints the total time it took for the user to type all ingredients, the user's score based on time,
    the amount of items the user correctly typed, the user's score based on typing accuracy,
    and the total score for this section.

    Returns:
    total_score(float): Value representing the user's score for this section that is calculated by the
    average of the user's time score and accuracy score.
    """
    total_items = 3 + len(order['cheese']) + len(order['toppings'])
    allowed_time = total_items * 2
    print(f"Type all ingredients in {allowed_time} seconds or less to receieve a perfect score.")
    print(f"{order}")
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Start!")

    loop = True
    while loop == True:
        start = time.time()
        crust_input = input("Type the crust: ")
        size_input = input("Type the size: ")
        sauce_input = input("Type the sauce: ")
        cheese_input = input("Type the cheese: ")
        toppings_input = input("Type the toppings: ")
        end = time.time() 
        loop = False
    total_time = round(end-start, 2)
    
    #time score
    if total_time <= allowed_time:
        time_score = 5
    else:
        # Deducts 0.1 points for each second over allowed time
        time_score =  round(5 - ((total_time - allowed_time) / 10), 2)
    
    #accuracy score
    individual_score = 5/total_items
    acc_score = 0
    correct_items = 0
    
    if crust_input.lower() == order['crust'].lower():
        acc_score += individual_score
        correct_items += 1

    if size_input.lower() == order['size'].lower():
        acc_score += individual_score
        correct_items += 1

    if sauce_input.lower() == order['sauce'].lower():
        acc_score += individual_score
        correct_items += 1

    cheese_list = [item.strip().lower() for item in cheese_input.split(",")]
    for item in cheese_list:
        if item.lower() in {item.lower() for item in order['cheese']}:
            acc_score += individual_score
            correct_items += 1

    toppings_list = [item.strip().lower() for item in toppings_input.split(",")]
    for item in toppings_list:
        if item.lower() in {item.lower() for item in order['toppings']}:
            acc_score += individual_score
            correct_items += 1
    
    total_score = round((time_score + acc_score)/2, 2)
    print("\n")
    print(f"You took {total_time} second to prepare the ingredients.")
    print(f"Time score: {time_score}/5.0")
    print(f"You correctly prepared {correct_items} items out of {total_items}.")
    print(f"Accuracy score: {acc_score}/5.0")
    print(f"Your total score is {total_score}/5.0")
    return total_score

pizza_prep()

class InputOutputHandler:
    """
    A class to calculate a final rating for a pizza based on the chef's actions during preparation, cooking, 
    and slicing stages. 
    """

    def cooking_system(self, cooking_time, ideal_time=10):
        """
        Calculates the cooking score based on the deviation from an ideal cooking time.
        Args:
            cooking_time (float): The actual cooking time for the pizza.
            ideal_time (int, optional): The ideal cooking time (default is 10 minutes).
        Returns:
            int: The cooking score based on the deviation from the ideal time.
        """
        deviations = list(range(7))  
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        return cooking_score

    def slicing_system(self, slices, preferred_slices=8):
        """
        Calculates the slicing score based on how the number of slices compares to the preferred number.
        Args:
            slices (int): The number of slices the pizza was cut into.
            preferred_slices (int, optional): The preferred number of slices (default is 8).
        Returns:
            int: The slicing score based on the difference from the preferred slice count.
        """
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score, prep_section_score):
        """
        Calculates the final pizza rating based on the average score of preparation, cooking, and slicing stages.
        Args:
            prep_score (int): The score for the pizza preparation phase.
            cooking_score (int): The score for the cooking phase.
            slicing_score (int): The score for the slicing phase.
            prep_section_score (int): The score for the preparation section.
        Returns:
            str: The final rating for the pizza.
        """
        total_score = prep_score + cooking_score + slicing_score + prep_section_score
        avg_score = total_score / 4
        
        return (
            "Perfect" if avg_score >= 4.5 else
            "Excellent" if avg_score >= 3.5 else
            "Okay" if avg_score >= 2.5 else
            "Bad" if avg_score >= 1.5 else
            "Terrible"
        )

    def process_order(self, customer):
        # Generate an order
        order = customer.generate_order()
        print("\n".join([str(value) for value in order.values()]))
        
        # Run pizza_prep for preparation phase
        print("Time to prep the pizza!")
        prep_section_score = pizza_prep()

        # Extract order details
        toppings = set(order['toppings'].split(", "))
        cook_time = float(order['cook_time'].split(" ")[2])
        slices = len(toppings)  

        # Calculate individual scores
        cooking_score = self.cooking_system(cook_time)
        slicing_score = self.slicing_system(slices)

        # Calculate final rating
        final_rating = self.calculate_final_rating(cooking_score, slicing_score, prep_section_score)
        print(f"\nFinal Rating for {order['name']}: {final_rating}")
