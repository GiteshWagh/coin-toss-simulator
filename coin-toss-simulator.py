# Coin Toss Simulator 🪙
# This program randomly prints "Heads" or "Tails" in the terminal

def coin_toss():   
    
    import random
    # List of two possible outcomes
    outcomes = ["Heads","Talis"]

    # Randomly choose one from the list
    result = random.choice(outcomes)

    # Print the result
    print("Tossing the coin...")
    print("\nResult:",result,"\n")
    return

# Call the function
coin_toss()