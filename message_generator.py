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
            "Je vous invite à vous abonner à notre page Instagram pour obtenir plus d’informations sur nous, et bénéficier de réductions spéciales",
            "Je vous invite à vous abonner à notre page Instagram pour découvrir plus d’informations sur nous et profiter de réductions exclusives.",
            "Rejoignez-nous sur Instagram pour en savoir plus sur nous et bénéficier de promotions spéciales réservées à nos abonnés.",
            "Nous vous invitons à suivre notre page Instagram pour obtenir des informations supplémentaires sur nous et bénéficier de réductions exclusives.",
            "Nous vous invitons à suivre notre page Instagram pour découvrir davantage d'informations sur nous et profiter de réductions exclusives.",
            "AROMAZE vous invite à vous abonner à notre page Instagram pour obtenir plus d’informations sur nos bougies et bénéficier de réductions spéciales.",
            "AROMAZE vous invite à vous abonner à notre page Instagram pour découvrir davantage sur nos bougies et profiter de réductions spéciales.",
            "Explorez notre collection exclusive de bougies parfumées. Suivez-nous sur Instagram pour ne rien manquer de nos nouveautés et bénéficier d'offres spéciales réservées à notre communauté.",
            "Abonnez-vous à notre Instagram pour découvrir nos bougies parfumées et profiter d'offres exclusives.",
            "Abonnez-vous à notre compte Instagram pour découvrir nos bougies parfumées et profiter de nos offres exclusives",
            "Abonnez-vous à notre compte Instagram pour bénéficier de réductions spéciales sur nos bougies parfumées",
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


