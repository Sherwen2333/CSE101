# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
class Package:
    def __init__(self, sender, recipient, cost=0, distance=0):
        self.sender = sender
        self.recipient = recipient
        self.cost = cost
        self.distance = distance

# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #

    def __repr__(self):
        return f'Package(\"{self.sender}\", \"{self.recipient}\", ' \
               f'cost={self.cost}, distance={self.distance})'

# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #

    def __eq__(self, other):
        return self.sender == other.sender and self.recipient == other.recipient and \
                self.cost == other.cost and abs(self.distance - other.distance) < 0.01

# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #