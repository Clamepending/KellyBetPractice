import random

def calculate_kelly_bet(p, odds, bankroll):
    b = odds
    q = 1 - p
    kelly_fraction = (b * p - q) / b
    kelly_bet = kelly_fraction * bankroll
    return kelly_bet

def calculate_expected_value(p, odds, stake):
    winnings = odds * stake
    ev = (p * winnings) - (1 - p) * stake
    return ev

def run_simulation(bankroll):
    while True:
        # Ask the user for the probability and odds
        p = float(input("Enter the probability as a decimal (e.g., 0.2 for 20%): "))
        odds_input = input("Enter the normalized odds in x:1 format (e.g., 3:1 enter 3): ")
        
        # Convert the odds input from string format "x:1" to a float
        odds = float(odds_input)
        
        # Display the inputted probabilities and odds
        print(f"Probability: {p}, Odds: {odds}:1")
        
        # Calculate optimal Kelly bet and EVs
        kelly_bet = calculate_kelly_bet(p, odds, bankroll)
        ev = calculate_expected_value(p, odds, kelly_bet)
        
        # Display the results
        print(f"Optimal Kelly Bet: ${kelly_bet:.3f}")
        print(f"Expected Value: ${ev:.3f}\n")
        
        # Wait for the user to press spacebar to move to the next opportunity
        input("Press spacebar for the next opportunity...")


# Run the simulation with an initial bankroll of $1000
run_simulation(1)
