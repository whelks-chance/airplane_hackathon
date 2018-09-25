import random


class Passenger:
    def __init__(self, luggage_chance=0.5, row_number=None, seat_number=None):
        self.relatives = []
        self.seat_number = seat_number
        self.row_number = row_number
        self.luggage_chance = luggage_chance
        self.lugagge_list = []
        self.generate_multiple_luggage(1)
        self.mobility = 1

    def __str__(self):
        return 'Passenger with Row {}, seat {}, luggage {}'.format(self.row_number, self.seat_number, self.lugagge_list)

    def generate_multiple_luggage(self, quantity):
        for i in range(0, quantity):
            new_luggage = self.generate_luggage()
            if new_luggage:
                self.lugagge_list.append(new_luggage)

    def generate_luggage(self):
        # Generates an luggage item if chance is above a dice roll
        dice_roll = random.uniform(0.0, 1.0)
        if dice_roll < self.luggage_chance:
            return Luggage()
        else:
            return None

    def related_to(self, passenger):
        self.relatives.append(passenger)

    def move_along_aisle(self):
        pass

    def add_luggage_to_overhead(self):
        pass

    def move_into_row(self):
        pass


class Luggage:
    def __init__(self):
        pass

    def __repr__(self):
        return 'A suitcase'
