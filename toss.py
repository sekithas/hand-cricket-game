import random
import time

#coin toss implementation

def toss():
    while True:
        print("\n")
        tossChoice = input("Heads or tails: ").lower()

        if tossChoice not in ["heads", "tails"]:
            print("Invalid input!")
            continue

        tossResult = random.choice(["heads", "tails"])

        print("\nFlipping coin", end="")
        for x in range(5):
            time.sleep(0.2)
            print(".", end="", flush=True) 
        print("\n")

        if tossChoice == tossResult:
            print("You won the toss!")

            while True:
                decision = input("Bat or ball?: ").lower()

                if decision in ["bat", "ball"]:
                    if decision == "bat":
                        return "user"
                    else:
                        return "computer"

                print("Invalid input!")

        else:
            print("Computer won the toss!")

            computerDecision = random.choice(["bat", "ball"])
            print(f"Computer chose to {computerDecision.upper()}!")

            if computerDecision == "bat":
                return "computer"
            else:
                return "user"
