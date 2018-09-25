

class Plane:
    def __init__(self, number_of_rows=15, seats_per_row=6, number_of_aisles=1, doors=1, overheads_per_row=2):
        self.doors = doors
        self.overheads_per_row = overheads_per_row
        self.number_of_rows = number_of_rows
        self.number_of_aisles = number_of_aisles
        self.seats_per_row = seats_per_row
        self.rows = []
        self.aisles = []

        for i in range(0, number_of_rows):
            self.rows.append(Row(seats_per_row))

        for j in range(0, self.number_of_aisles):
            self.aisles.append(Aisle(number_of_rows, position=Aisle.central_position))

    def __str__(self):
        return 'This plane has {} rows of seats.\n' \
               'The plane has {} doors.\n' \
               'Each row has {} seats.\n' \
               'Each row has {} overheads.\n' \
               'The plane has {} seats total\n' \
               'The plane has {} overheads total.\n'.format(
            self.number_of_rows,
            self.doors,
            self.seats_per_row,
            self.overheads_per_row,
            self.seats_on_plane(),
            self.overheads_on_plane()
        )

    def seats_on_plane(self):
        return self.number_of_rows * self.seats_per_row

    def overheads_on_plane(self):
        return self.number_of_rows * self.overheads_per_row

    def print_manifest(self):
        print('No info yet...')


class Row:
    def __init__(self, seats_per_row=6, overheads_per_row=2):
        self.seats = []
        self.overheads = []

        for i in range(0, seats_per_row):
            self.seats.append(Seat())

        for j in range(0, overheads_per_row):
            self.overheads.append(Overhead())


class Overhead:
    def __init__(self, capacity=2):
        self.capactity = capacity
        self.luggage_items = []

    def load(self, luggage_item):
        self.luggage_items.append(luggage_item)


class Seat:
    pass


class Door:
    pass


class Aisle:
    central_position = 1

    def __init__(self, number_of_rows, position=None):
        self.number_of_rows = number_of_rows
        if position:
            self.position = position
        else:
            self.position = self.central_position
