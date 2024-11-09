class InputOutputHandler:
     """
    A class to calculate a final rating for a pizza order based on chef's actions, including cooking time, slicing, 
    and toppings. The class takes optional parameters for ideal cooking time and preferred slice count.
    """
def calculate_prep_score(self, toppings, ideal_toppings={"pepperoni", "mushrooms", "extra cheese"}):
        """
        Calculates a preparation score based on the toppings chosen by the chef.
        Parameters:
        toppings : set
            The toppings chosen for the pizza.
        ideal_toppings : set, optional
            The ideal set of toppings for this pizza.

        Returns:
        int
            A score from 1 (poor topping choice) to 5 (ideal topping choice).
        """
        matching_toppings = ideal_toppings & toppings
        prep_score = min(5, max(1, int(5 * (len(matching_toppings) / len(ideal_toppings)))))
        return prep_score
    
def calculate_cooking_score(self, cooking_time, ideal_time=10):
        """
        Scores the cooking stage based on how close the cooking time is to the ideal cooking time.
        Parameters:
        cooking_time : int
            The time the pizza was left in the oven
        ideal_time : int, optional
            The ideal cooking time for the pizza
        Returns:
        int
            A score from 1 (burned/undercooked) to 5 (perfectly cooked).
        """
        # Map time deviation to different scores
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        cooking_score = score_map.get(abs(cooking_time - ideal_time), 1)
        return cooking_score

def calculate_slicing_score(self, slices, preferred_slices=8):
    
        slicing_score = max(1, 5 - abs(slices - preferred_slices))
        return slicing_score
    
def calculate_final_rating(self, prep_score, cooking_score, slicing_score):
    
        # Calculate the average score from all stages
        avg_score = (prep_score + cooking_score + slicing_score) / 3
        
        # Determine the rating based on the average score
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
        