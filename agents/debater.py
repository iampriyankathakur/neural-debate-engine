import random

class DebaterAgent:

    def __init__(self, name, stance):
        self.name = name
        self.stance = stance

    def generate_argument(self, topic):

        supporting_points = {
            "for": [
                "improves scalability",
                "increases efficiency",
                "enhances accessibility",
                "reduces costs",
                "enables personalization"
            ],
            "against": [
                "reduces human connection",
                "creates ethical risks",
                "increases dependency",
                "can amplify inequality",
                "removes emotional intelligence"
            ]
        }

        point = random.choice(supporting_points[self.stance])

        argument = (
            f"{self.name} argues that {topic.lower()} "
            f"{point} and significantly impacts society."
        )

        return argument
