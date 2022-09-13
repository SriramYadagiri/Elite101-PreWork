import random

badJokes = [
    "What do you call a python which is exactly 3.14m long ?:A πthon",
    "How do you organize an astronomer's party?:You planet.",
    "What do you call a pony with a sore throat?:A little hoarse.",
    "Why should you never eat a clock?:Because it's too time-consuming."
]

endOfJokes = ["Ha Ha Ha Ha!", "Why aren't you laughing.", "Sorry"]


def printJoke():
    joke = random.choice(badJokes).split(":")
    print(joke[0])
    print(joke[1])
    print(random.choice(endOfJokes))
