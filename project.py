from toss import toss
from commentaries import commentary
import random
import tabulate

#core mechanism of hand cricket

def main():
    print("\n")
    print("Welcome to hand cricket!")
    print("Each player gets 2 overs | 3 wickets")

    firstBatter = toss()
    secondBatter = otherPlayer(firstBatter)

    print("\n")
    print("=" * 10 + " FIRST INNINGS " + "=" * 10)
    firstScore = innings(firstBatter)

    target = firstScore[0] + 1

    print("\n")
    print("=" * 10 + " SECOND INNINGS " + "=" * 10)
    secondScore = innings(secondBatter, target)

    showResult(firstBatter, firstScore, secondScore)


def otherPlayer(player):
    if player == "user":
        return "computer"
    return "user"


def innings(batter, target=None):

    name = "You" if batter == "user" else "Computer"
    print(f"\n{name} are batting now!\n")

    balls = 0
    wickets = 0
    score = 0
    bowlingHistory = []

    if target is not None:
        print(f"{name} need {target} runs to win!\n")

    while balls < 12 and wickets < 3:
        try:
            userRuns = int(input("Runs: "))
            if 0 <= userRuns <= 6:
                computerRuns = random.choice([0,1,2,2,2,3,4,4,4,5,5,6,6,6,6])

                balls += 1

                print(f"Computer runs: {computerRuns}")

                if computerRuns == userRuns:
                    wickets += 1
                    print(commentary("OUT"))
                    bowlingHistory.append("W")
                    print(f"{name} has {3 - wickets} wickets remaining!")
                    continue

                if batter == "user":
                    score += userRuns
                    print(commentary(userRuns))
                    bowlingHistory.append(userRuns)
                else:
                    score += computerRuns
                    print(commentary(computerRuns))
                    bowlingHistory.append(computerRuns)

                print(f"{score} - {wickets}")

                if target is not None and score >= target:
                    break

            else:
                print("Invalid runs, runs should be between 0-6!")

        except ValueError:
            print("Invalid runs, runs should be an integer!")

    print("\n")
    print("="*10, "INNINGS RESULTS", "="*10)
    print(tabulate.tabulate([["Runs", "Wickets Fallen"], [score, wickets]], headers = "firstrow", tablefmt = "grid"))
    print(f"Last {len(bowlingHistory)} balls: \n", *bowlingHistory)

    return (score, wickets)


def showResult(firstBatter, firstScore, secondScore):
    print("\nA long day comes to an end!\n")

    if firstBatter == "user":
        userScore, userWickets = firstScore
        computerScore, computerWickets = secondScore
    else:
        userScore, userWickets = secondScore
        computerScore, computerWickets = firstScore

    print("="*10, "FINAL SCOREBOARD", "="*10)
    print(tabulate.tabulate([["You", userScore, userWickets],["Computer", computerScore, computerWickets]], headers=["Player", "Runs", "Wickets Fallen"], tablefmt="grid"))

    if userScore > computerScore:
        print(f"\nYou win by {userScore - computerScore} runs!")
    elif userScore < computerScore:
        print(f"\nComputer wins by {computerScore - userScore} runs!")
    else:
        print("\nIt's a tie!")

    print("\n")

if __name__ == "__main__":
    main()
