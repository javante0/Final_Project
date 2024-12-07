from collections import defaultdict
import time
import random

class InputOutputHandler:
    """
    Handles input and output for the Pizza Game, scoring, and user interactions.

    Note: This class depends on external components:
    - pizza_prep() function (from John's code) for preparation scoring
    - Customer class (from Dan's code) for order generation
    """
    def __init__(self):
        self.customer_name = None

    def welcome_message(self):
        """
        Displays a welcome message to the player.

        Side Effects:
        - Prints a welcome message to the console
        - Uses the customer's name stored in self.customer_name
        """
        print("\nWelcome to the Pizza Game!")
        print(f"Hello, {self.customer_name}! Ready to show off your pizza skills?")

    def explain_rules(self):
        """
        Prints out the rules of the Pizza Game.

        Side Effects:
        Prints game rules to the console
        """
        print("\n--- Game Rules ---")
        print("1. You will prepare a pizza by typing the requested ingredients as fast as you can.")
        print("2. After preparation, you will choose how long to cook the pizza.")
        print("3. Finally, you will decide how many slices to cut the pizza into.")
        print("4. Your performance will be scored in each stage. Try to get a 'Perfect' rating!")
    # Sorry Dan, gotta use this
        #Prep score for number of toppings
    def calculate_prep_score(self, toppings_set):
        """
        Calculates a score based on the number of pizza toppings.

        Argument:
            toppings_set (set): A set of toppings added to the pizza

        Returns:
            int: A score between 1 and 5 representing the preparation quality
            (5 points for 5 or more toppings, otherwise equal to number of toppings)
        """
        max_toppings_score = 5
        num_toppings = len(toppings_set)
        return min(num_toppings, max_toppings_score)

    def cooking_system(self, cooking_time, ideal_time):
        """
        Evaluates the cooking time against an ideal cooking time.

        Args:
            cooking_time (float): The time the user cooked the pizza
            ideal_time (float): The recommended cooking time for the pizza

        Returns:
            int: A score between 1 and 5 based on how close the cooking time is to the ideal time
        """
        deviations = list(range(7))
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        # One for me
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        return cooking_score

    def slicing_system(self, slices, preferred_slices):
        """
        Evaluates the number of pizza slices against preferred slice count.

        Args:
            slices (int): The number of slices the pizza was cut into
            preferred_slices (int): The recommended number of slices

        Returns:
            int: A score between 1 and 5 based on how close the slice count is to the preferred number
        """
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score, prep_section_score):
        """
        Calculates the overall pizza rating based on scores from different stages.

        Arguments:
            prep_score (int): Score for pizza preparation
            cooking_score (int): Score for cooking time
            slicing_score (int): Score for slicing
            prep_section_score (int): Score from the pizza preparation section

        Returns:
            str: A rating of "Perfect", "Excellent", "Okay", "Bad", or "Terrible"
                 based on the average of the input scores
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
        """
        Processes a complete pizza order, managing all stages of pizza creation.

        Arguments:
            customer (Customer): A customer object from Dan's code with order generation capability

        Dependencies:
        - Requires pizza_prep() function from John's code
        - Requires generate_order() method from Customer class

        Side Effects:
        - Prints order details, game instructions, and scores
        - Takes user input for cooking time and slice count
        - May use default values if user input is invalid
        """
        order = customer.generate_order()
        ideal_cooking_time = random.randint(8, 12)  # Randomize ideal cooking time
        preferred_slices = random.randint(6, 12)  # Randomize ideal slice count

        print(f"\nOrder Details: {customer}")
        print(f"Ideal cooking time: {ideal_cooking_time} minutes")
        print(f"Preferred number of slices: {preferred_slices}")

        # Run pizza preparation
        print("\nTime to prep the pizza!")
        #Relies on the pizza_prep function in John's part of the code
        prep_section_score = pizza_prep(order)

        # Calculate preparation score based on toppings
        prep_score = self.calculate_prep_score(set(order['toppings']))

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
            prep_section_score
        )

        # Print all scores and the final rating
        print("\n--- Score Breakdown ---")
        print(f"Preparation Score: {prep_score}/5")
        print(f"Cooking Score: {cooking_score}/5")
        print(f"Slicing Score: {slicing_score}/5")
        print(f"Prep Section Score: {prep_section_score}/5")
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
        #
        parser = argparse.ArgumentParser(description="Pizza Game Input Handler")
        parser.add_argument("name", type=str, help="Your name")
        args = parser.parse_args()

        #Relies on the customer class in Dan's code
        customer = Customer(args.name)

    
        handler = InputOutputHandler()
        handler.customer_name = args.name

    # Run the game
        handler.run(customer)