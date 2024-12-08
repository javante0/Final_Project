import argparse
from collections import defaultdict
import time
import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []
        self.probability_chain = {}
        self.crust_options = ['thin', 'thick', 'stuffed']
        self.size_options = ['small', 'medium', 'large']
        self.sauce_options = ['marinara', 'buffalo', 'barbeque', 'pesto']
        self.cheese_options = ['mozzarella', 'cheddar', 'parmesan']
        self.toppings = ['pepperoni', 'mushroom', 'onion', 'olive', 'pineapple', 'sausage', 'bacon', 'anchovy', 'spinach']
        for topping in self.toppings:
            self.probability_chain[topping] = {}
            for next_topping in self.toppings:
                self.probability_chain[topping][next_topping] = 1 / len(self.toppings)

    def generate_order(self):
        self.crust_type = random.choice(self.crust_options)
        self.size_type = random.choice(self.size_options)
        self.sauce_type = random.choice(self.sauce_options)
        self.cheese_type = random.choice(self.cheese_options)
        self.selected_toppings = []
        num_toppings = random.randint(2, 5)
        first_topping = random.choice(self.toppings)
                
        for topping in range(num_toppings):
            self.selected_toppings.append(first_topping)
            next_topping = random.choices(
                self.toppings,
                weights = [self.probability_chain[first_topping][t] for t in self.toppings])[0]
            first_topping = next_topping
                
        for topping in range(len(self.selected_toppings) - 1):
            current = self.selected_toppings[topping]
            next_item = self.selected_toppings[topping + 1]
            if next_item not in self.probability_chain[current]:
                self.probability_chain[current][next_item] = 0
            self.probability_chain[current][next_item] += 1
                
        for topping, transitions in self.probability_chain.items():
            total = sum(transitions.values())
            for next_topping in transitions:
                transitions[next_topping] /= total
                
        self.cook_time = 6
        self.cook_time += 1.5 if self.crust_type == 'stuffed' else 1 if self.crust_type == 'thick' else 0
        self.cook_time += len(self.selected_toppings) * 0.6
        self.cook_time = round(self.cook_time, 1)

        order = {
                'name': self.name,
                'crust': self.crust_type,
                'size': self.size_type,
                'sauce': self.sauce_type,
                'cheese': self.cheese_type,
                'toppings': self.selected_toppings,
                'cook_time': self.cook_time
        }
        self.order_history.append(order)
        return order
        
    def __str__(self):
        ticket = {
                'separator1': "---------------------------------",
                'name': f"{self.name}'s ORDER",
                'separator2': "---------------------------------",
                'crust': f"Crust: {self.crust_type}",
                'size': f"Size: {self.size_type}",
                'sauce': f"Sauce: {self.sauce_type}",
                'cheese': f"Cheese: {self.cheese_type}",
                'toppings': f"Ingredients: {self.selected_toppings}",
                'cook_time': f"Cook for {self.cook_time} minutes",
                'separator3': "---------------------------------"
                }
        
        return "\n".join(ticket.values())


def pizza_prep(order):
    total_items = 4 + len(order['toppings'])
    allowed_time = total_items * 2
    print(f"Type all ingredients in {allowed_time} seconds or less to receive a perfect score.")
    buffer = input("\nPress the enter key to continue.")
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Start!")

    start = time.time()
    crust_input = input("Type the crust: ")
    size_input = input("Type the size: ")
    sauce_input = input("Type the sauce: ")
    cheese_input = input("Type the cheese: ")
    toppings_input = input("Type the toppings: ")
    end = time.time()
    total_time = round(end - start, 2)
    
    # Time score
    time_score = 5.0 if total_time <= allowed_time else round(5 - ((total_time - allowed_time) / 10), 2)

    # Accuracy score
    individual_score = 5 / total_items
    acc_score = 0
    correct_items = 0

    if crust_input.lower() == order.get('crust').lower():
        acc_score += individual_score
        correct_items += 1

    if size_input.lower() == order.get('size').lower():
        acc_score += individual_score
        correct_items += 1

    if sauce_input.lower() == order.get('sauce').lower():
        acc_score += individual_score
        correct_items += 1

    if cheese_input.lower() == order.get('cheese').lower():
        acc_score += individual_score
        correct_items += 1

    toppings_list = [item.strip().lower() for item in toppings_input.split(",")]
    for item in toppings_list:
        if item.lower() in {t.lower() for t in order.get('toppings')}:
            acc_score += individual_score
            correct_items += 1

    total_score = round((time_score + acc_score) / 2, 2)
    print("\n")
    print(f"You took {total_time} seconds to prepare the ingredients.")
    print(f"Time score: {round(time_score,2)}/5.0")
    print(f"You correctly prepared {correct_items} items out of {total_items}.")
    print(f"Accuracy score: {round(acc_score,2)}/5.0")
    print(f"Your total score is {total_score}/5.0")
    return total_score


class InputOutputHandler:
    def __init__(self):
        self.customer_name = None

    def welcome_message(self):
        print("\nWelcome to the Pizza Game!")
        print(f"Hello, {self.customer_name}! Ready to show off your pizza skills?")
        time.sleep(2)

    def explain_rules(self):
        print("\n--- Game Rules ---")
        print("1. You will prepare a pizza by typing the requested ingredients as fast as you can.")
        print("2. After preparation, you will choose how long to cook the pizza.")
        print("3. Finally, you will decide how many slices to cut the pizza into.")
        print("4. Your performance will be scored in each stage. Try to get a 'Perfect' rating!")
        buffer = input("\nPress the enter key to continue.")

    def calculate_prep_score(self, toppings_set):
        max_toppings_score = 5
        num_toppings = len(toppings_set)
        return min(num_toppings, max_toppings_score)

    def cooking_system(self, cooking_time, ideal_time):
        deviations = list(range(7))
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        # One for me
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        return cooking_score

    def slicing_system(self, slices, preferred_slices):
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score):
        total_score = cooking_score + slicing_score + prep_score
        avg_score = total_score / 3
        return (
            "Perfect" if avg_score >= 4.5 else
            "Excellent" if avg_score >= 3.5 else
            "Okay" if avg_score >= 2.5 else
            "Bad" if avg_score >= 1.5 else
            "Terrible"
        )

    def process_order(self, customer):
        order = customer.generate_order()
        ideal_cooking_time = random.randint(8, 12)  # Randomize ideal cooking time
        preferred_slices = random.randint(6, 12)  # Randomize ideal slice count

        print(f"\nOrder Details: {customer}")
        print(f"Ideal cooking time: {ideal_cooking_time} minutes")
        print(f"Preferred number of slices: {preferred_slices}")

        # Run pizza preparation
        print("\nTime to prep the pizza!")
        prep_score = pizza_prep(order)

        # Ask user for cooking time
        try:
            cooking_time = float(input("How many minutes do you want to cook the pizza? "))
        except ValueError:
            #If they fail to put a valid input, the default is 10 minutes
            print("Invalid input, using default cooking time (10 minutes).")
            cooking_time = 10.0

        cooking_score = self.cooking_system(cooking_time, ideal_cooking_time)

        # slicing score
        try:
            slices = int(input("How many slices was the pizza cut into? "))
        except ValueError:
            #Like if the cooking time, if failture, default is 8 slices
            print("Invalid input, using default preferred slices (8).")
            slices = 8

        slicing_score = self.slicing_system(slices, preferred_slices)

        # Final rating, yipee
        final_rating = self.calculate_final_rating(
            prep_score, 
            cooking_score, 
            slicing_score, 
        )

        # Print all scores and the final rating
        print("\n--- Score Breakdown ---")
        print(f"Preparation Score: {prep_score}/5")
        print(f"Cooking Score: {cooking_score}/5")
        print(f"Slicing Score: {slicing_score}/5")
        print(f"\nFinal Rating for {order['name']}: {final_rating}")
        
    #this part sucked to firgure out
    def run(self, customer):
        self.welcome_message()
        self.explain_rules()
        play_again = True
        while play_again:
            self.process_order(customer)
            user_input = input("\nWould you like to play again? (yes or no): ").strip().lower()
            if user_input != "yes":
                play_again = False
                print("\nThank you for playing our Pizza Game! See ya!")

    #This part sucked even more as I testing it in juptyer notebook
if __name__ == "__main__":
        # Standard argparse for command-line usage
        parser = argparse.ArgumentParser(description="Pizza Game Input Handler")
        parser.add_argument("name", type=str, help="Your name")
        args = parser.parse_args()


        customer = Customer(args.name)

    
        handler = InputOutputHandler()
        handler.customer_name = args.name

    # Run the game
        handler.run(customer)
