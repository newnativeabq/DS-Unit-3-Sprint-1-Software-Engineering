import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        if identifier == None:
            self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        ratio = self.flammability * self.weight
        message_options = {
            0: "...fizzle.",
            1: "...boom!",
            2: "...BABOOM!!",
            }
        ratio_breakpoints = [0, 10, 50]
        return message_options[get_message_level(ratio, ratio_breakpoints)]


class BoxingGlove(Product):
    def __init__(self, name, weight=10):
        super().__init__(name, weight)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        ratio = self.weight
        message_options = {
            0: "That tickles.",
            1: "Hey that hurt!",
            2: "OUCH!",
            }
        ratio_breakpoints = [0, 5, 15]
        return message_options[get_message_level(ratio, ratio_breakpoints)]



def get_message_level(ratio, ratio_breakpoints):
    for level, breakpoint in enumerate(ratio_breakpoints):
        if ratio > breakpoint:
            message_level = level
        elif ratio < breakpoint:
            break
    return message_level
