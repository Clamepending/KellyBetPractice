import random
import matplotlib.pyplot as plt

def calculate_kelly_bet(p, odds, bankroll):
    b = odds
    q = 1 - p
    kelly_fraction = (b * p - q) / b
    kelly_bet = kelly_fraction * bankroll # Ensure bet is not negative
    return max(kelly_bet, 0)

def calculate_expected_value(p, odds, stake):
    winnings = odds * stake
    ev = (p * winnings) - (1 - p) * stake
    return ev

def simulate_bet(p, odds, stake, kelly_stake):
    # Simulate the outcome of the bet
    result = random.random() < p  # True if the bet is won, False if lost
    if result:
        return stake * odds, kelly_stake * odds  # Win
    else:
        return -stake, -kelly_stake  # Loss

def run_simulation(bankroll, games):
    winnings = [bankroll]  # List to store bankroll after each round
    kelly_winnings = [bankroll]  # List to store bankroll using Kelly criterion after each round
    
    for round_num in range(1, games + 1):  # Run the number of specified rounds
        # Randomly generate probabilities and odds
        p = round(random.uniform(0.01, 0.3), 2)
        odds = round(random.uniform(0.5, 13.0), 1)
        
        # Display the randomly generated probabilities and odds 
        print(f"Round {round_num}: Probability: {p}, Odds: {odds}:1")
        
        # Ask the user for their bet amount
        bet = float(input(f"Enter your bet amount (Bankroll: ${bankroll:.2f}): "))

        # Calculate the optimal Kelly bet for the user's bankroll
        kelly_bet = calculate_kelly_bet(p, odds, kelly_winnings[-1])  # Use Kelly bankroll
        print(f"Optimal Kelly Bet: ${kelly_bet:.2f}")
        
        # Simulate the user bet
        user_result, kelly_result = simulate_bet(p, odds, bet, kelly_bet)
        bankroll += user_result
        winnings.append(bankroll)
        
        kelly_bankroll = kelly_winnings[-1] + kelly_result
        kelly_winnings.append(kelly_bankroll)
        
        # Display the result of the bet and updated bankroll
        if user_result > 0:
            print(f"You won! Your winnings are ${user_result:.2f}.")
        else:
            print(f"You lost! Your loss is ${-user_result:.2f}.")
        
        print(f"Updated Bankroll: ${bankroll:.2f}")
        print(f"Kelly Bankroll: ${kelly_bankroll:.2f}\n")
    
    # Plot the bankroll over the rounds
    plt.plot(range(1, games + 2), winnings, marker='o', label='Your Bankroll')
    plt.plot(range(1, games + 2), kelly_winnings, marker='o', color='yellow', label='Kelly Bankroll')
    plt.title('Bankroll Over 10 Rounds')
    plt.xlabel('Round Number')
    plt.ylabel('Bankroll ($)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the simulation with an initial bankroll of $1000 for 10 rounds
run_simulation(1000, 10)
