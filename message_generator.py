import random


class MessageGenerator:
    def __init__(self):
        self.greetings = [
            "Bonjour",
            "Salut",
            "Coucou",
            "Bonne journée",
            "Bon matin",
            "Bonsoir",
            "Bonne soirée",
            "Salut tout le monde",
            "Bonjour à tous",
        ]
        self.introductions = [
            "how are you today?",
            "what's up?",
            "how's it going?",
            "hope you're doing well."
        ]
        self.statements = [
            "Python is fun!",
            "Keep up the good work!",
            "Have a great day!",
            "You're doing awesome!"
        ]
        self.closings = [
            "Goodbye!",
            "See you later!",
            "Take care!",
            "Have a nice day!"
        ]

    def generate_random_message(self):
        greeting = random.choice(self.greetings)
        introduction = random.choice(self.introductions)
        statement = random.choice(self.statements)
        closing = random.choice(self.closings)

        message = f"{greeting}, {introduction} {statement} {closing}"
        return message


