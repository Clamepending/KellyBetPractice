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
        # Randomly generate probabilities and odds for the sake of the simulation
        p = round(random.uniform(0.01, 0.3), 2)
        odds = round(random.uniform(0.5, 13.0), 1)
        
        # Display probabilities and odds
        print(f"Probability: {p}, Odds: {odds}:1")
        
        # Wait for the user to press spacebar to calculate and show the answer
        input("Press spacebar when you're ready to see the answer...")
        
        # Calculate optimal Kelly bet and EVs
        kelly_bet = calculate_kelly_bet(p, odds, bankroll)
        ev = calculate_expected_value(p, odds, kelly_bet)
        
        # Display the results
        print(f"Optimal Kelly Bet: ${kelly_bet:.2f}")
        print(f"Expected Value: ${ev:.2f}\n")
        
        # Wait for the user to press spacebar to move to the next opportunity
        input("Press spacebar for the next opportunity...")

# Run the simulation with an initial bankroll of $1000
run_simulation(1000)
