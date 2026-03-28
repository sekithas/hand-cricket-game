import random

#dictionary containing common cricket commentaries

def commentary(run):
    commentary = {
        0: [
            "That’s another dot, the pressure is mounting on the batsman.",
            "Spot on from the bowler, just probing away. Good length, no room."
        ],
        1: [
            "Quick single taken.",
            "They rotate the strike with a single."
        ],
        2: [
            "Good running between the wickets for two.",
            "They come back for the second run comfortably."
        ],
        3: [
            "Excellent placement! They run three.",
            "Chased in the deep, and they pick up three runs."
        ],
        4: [
            "FOUR! Beautiful shot! That's a boundary.",
            "Cracked through the gap for four."
        ],
        5: [
            "Overthrows! They collect five runs.",
            "Misfield leads to five runs."
        ],
        6: [
            "That's huge! Six runs!",
            "SIX! Launched over the boundary for a maximum.",
            "SIX! BANG! Into the crowd!"
        ],
        "OUT": [
            "OUT! Taken! Excellent catch!",
            "OUT! Straight through the gate!"
        ],

        "HAT": [
            "HAT TRICK! Three in three!",
            "HAT TRICK! The stadium has gone wild."
        ]
        }
    return random.choice(commentary[run])
