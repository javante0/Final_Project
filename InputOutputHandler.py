class InputOutputHandler:
    """
    A class to calculate a final rating for a pizza based on the chef's actions
    during preparation, cooking, and slicing stages. Each stage contributes a score, and the final
    rating is calculated based on the average of these scores.
    """
    def calculate_prep_score(self, toppings, ideal_toppings={"pepperoni", "mushrooms", "extra cheese"}):
        """
        Calculates a preparation score based on the toppings chosen by the chef in 
        comparison to the ideal toppings.
        
        Arguments:
            toppings : set
            The toppings selected for the pizza.
        ideal_toppings : set, optional
            The ideal set of toppings for a high preparation score
            (default is {"pepperoni", "mushrooms", "extra cheese"}).
        Returns:
            (int) A score from 1 (poor topping choice) to 5 (ideal topping choice).
        """
        matching_toppings = ideal_toppings & toppings
        prep_score = min(5, max(1, int(5 * (len(matching_toppings) / len(ideal_toppings)))))
        return prep_score

    def cooking_system(self, cooking_time, ideal_time=10):
        """
        Scores the cooking stage based on how closely the cooking time aligns with 
        the ideal cooking time.
        
        Arguments:
            cooking_time : int
            The time the pizza was cooked in the oven.
        ideal_time : int, optional
            The ideal cooking time for the pizza (default is 10).
        Returns:
            (int) A score from 1 (burned/undercooked) to 5 (perfectly cooked).
        """
        deviations = list(range(7))  
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        
        return cooking_score

    def slicing_system(self, slices, preferred_slices=8):
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        """
        Scores the slicing stage based on how closely the slice count matches the preferred 
        number of slices.
        Arguments:
        slices : int
            The number of slices the pizza was cut into.
        preferred_slices : int, optional
            The preferred number of slices for a high slicing score (default is 8).
        Returns:
            (int) A score from 1 (poor slicing) to 5 (ideal slicing).
        """
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score):
        """
        Calculates the final rating by averaging the scores from each stage 
        (preparation, cooking, and slicing). Outputs a descriptive rating based 
        on the average score.
        
        Arguments:
        prep_score : int
            The preparation score from the toppings selection.
        cooking_score : int
            The cooking score based on cooking time.
        slicing_score : int
            The slicing score based on the number of slices.
        
        Returns:
            (str) A final rating as a string, ranging from "Perfect" to "Terrible." 
        """
        total_score = prep_score + cooking_score + slicing_score
        avg_score = total_score / 3
        
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
handler_test = InputOutputHandler()

prep_score = handler_test.calculate_prep_score({"pepperoni", "mushrooms", "extra cheese"})
cooking_score = handler_test.cooking_system(11)
slicing_score = handler_test.slicing_system(7) 

final_rating = handler_test.calculate_final_rating(prep_score, cooking_score, slicing_score)
print(f"Final Rating: {final_rating}")
            
