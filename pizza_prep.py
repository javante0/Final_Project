import time
import statistics

#will actually use dictionary from Customer class
order = {
            'name': "John",
            'crust': "Cheesy",
            'size': "Large",
            'sauce': "Marinara",
            'cheese': {"Cheddar"},
            'toppings': {"Pepperoni", "Bacon"},
}

def pizza_prep():
    print("Type all ingredients in 10 seconds or less to receieve a perfect score.")
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
    if total_time <= 10:
        time_score = 5
    else:
        time_score =  5 - ((total_time - 10) / 10)
    
    #accuracy score
    acc_score = 0
    cheese_score = 0
    topping_score = 0
    if crust_input.lower() == order['crust'].lower():
        acc_score += 1
    if size_input.lower() == order['size'].lower():
        acc_score += 1
    if sauce_input.lower() == order['sauce'].lower():
        acc_score += 1
    for item in cheese_input.strip().split(","):
        if item.lower() in {item.lower() for item in order['cheese']}:
            acc_score += 1/len(order['cheese'])
            cheese_score += 1
    for item in toppings_input.strip().split(","):
        if item.lower() in {item.lower() for item in order['toppings']}:
            acc_score += 1/len(order['toppings'])
            topping_score += 1
    
    total_score = round((time_score + acc_score)/2, 2)
    print(time_score)
    print(acc_score)
    print(cheese_score)
    print(topping_score)
    print(f"Your total score is {total_score}/5")
    return total_score

pizza_prep()