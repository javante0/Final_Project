How to run the game:

Run the program using the following command:

python Alpha_chefs_code.py.py (Any name here)

Purpose of each file:

pizza_prep.py:
This file contains the pizza_prep function, which has the pizza preparation phase of the game. The player is prompted to type the ingredients for the pizza (crust, size, sauce, cheese, and toppings). Their performance is scored based on the speed and accuracy of their inputs. The purpose is to gamify the preparation process by making it interactive and timed.

customer.py:
This file defines the Customer class, which manages customer specific data, such as the name, order history, and generated orders. It also simulates random pizza orders by selecting crusts, sauces, cheeses, and toppings using probabilities. The purpose is to create dynamic and realistic pizza orders for the game.

input_output_handler.py:
This file defines the InputOutputHandler class, which coordinates the flow of the game. It handles the user interface by displaying welcome messages, explaining the rules, and managing the cooking and slicing phases. It also calculates the final score based on the player’s performance in all stages. The purpose is to integrate all components of the game and provide a neat user experience.


| Method/Function    | Author |  Techniques Demonstrated |
-----------------------------------------------------------
| pizza_prep| John   |Comprehension|
| Customer.__str__  | Daniel | Magic method, f-string|
| InputOutputHandler.run | Terrence | ArgumentParser|
| InputOutputHandler.cooking_system | Terrence  | Optional parameters|
| InputOutputHandler.calculate_final_rating | John |Conditional expression|

