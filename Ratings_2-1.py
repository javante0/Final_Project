class InputOutputHandler2:
    def calculate_prep_score(self, toppings, ideal_toppings={"pepperoni", "mushrooms", "extra cheese"}):
        matching_toppings = ideal_toppings & toppings
        prep_score = min(5, max(1, int(5 * (len(matching_toppings) / len(ideal_toppings)))))
        return prep_score

    def cooking_system(self, cooking_time, ideal_time=10):
        deviations = list(range(7))  # Allowable deviations up to 6 minutes
        score_map = {0: 5, 1: 4, 2: 4, 3: 3, 4: 3, 5: 2, 6: 2}
        
        # Using a comprehension to get scores for each deviation and select the closest match
        cooking_score = score_map.get(min(deviations, key=lambda x: abs(cooking_time - ideal_time - x)), 1)
        
        return cooking_score

    def slicing_system(self, slices, preferred_slices=8):
        slice_diffs = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        
        # Using a set difference to determine the score based on slices
        slice_diff = abs(slices - preferred_slices)
        slicing_score = slice_diffs.get(slice_diff, 1)
        
        return slicing_score

    def calculate_final_rating(self, prep_score, cooking_score, slicing_score):
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