from collections import defaultdict
import time
import random

class InputOutputHandler:
    """
    A class to calculate a final rating for a pizza based on the chef's actions during preparation, cooking, 
    and slicing stages. Each stage contributes a score, and the final rating is calculated based on the 
    average of these scores.
    """

    def cooking_system(self, cooking_time, ideal_time=10):
        deviations = list(range(7))  
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        return cooking_score

    def slicing_system(self, slices, preferred_slices=8):
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score, prep_section_score):
        total_score = prep_score + cooking_score + slicing_score + prep_section_score
        avg_score = total_score / 4
        
        if avg_score >= 4.5:
            return "Perfect"
        elif avg_score >= 3.5:
            return "Excellent"
        elif avg_score >= 2.5:
            return "Okay"
        elif avg_score >= 1.5:
            return "Bad"
        else:
            return "Terrible"

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
        prep_score = self.calculate_prep_score(toppings)
        cooking_score = self.cooking_system(cook_time)
        slicing_score = self.slicing_system(slices)

        # Calculate final rating
        final_rating = self.calculate_final_rating(prep_score, cooking_score, slicing_score, prep_section_score)
        print(f"\nFinal Rating for {order['name']}: {final_rating}")
