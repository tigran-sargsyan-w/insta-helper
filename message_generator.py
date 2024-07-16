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
            "J'espère que vous allez bien.",
            "J'espère que tout va bien pour vous.",
            "J'espère que vous passez une bonne journée.",
            "Je vous souhaite une excellente journée.",
            "J'espère que tout se passe bien pour vous.",
            "Je vous souhaite une bonne journée.",
            "Je vous souhaite une journée agréable.",
            "J'espère que vous passez une agréable journée.",
        ]
        self.statements = [
            "Python is fun!",
            "Keep up the good work!",
            "Have a great day!",
            "You're doing awesome!"
        ]
        self.closings = [
            "Au revoir !",
            "À bientôt !",
            "Prenez soin de vous !",
            "Bonne journée !",
            "Passez une bonne journée !",
            "Bon week-end !",
            "À plus tard !",
            "Bonne soirée !",
            "Bon après-midi !",
            "Profitez bien de votre journée !",
            "Prenez soin de vous et à bientôt !",
            "Merci et à bientôt !",
            "À très bientôt !",
            "Cordialement !",
        ]

    def generate_random_message(self):
        greeting = random.choice(self.greetings)
        introduction = random.choice(self.introductions)
        statement = random.choice(self.statements)
        closing = random.choice(self.closings)

        message = f"{greeting}, {introduction} {statement} {closing}"
        return message


