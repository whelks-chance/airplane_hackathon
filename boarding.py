import random

from boarding_process import BoardingProcess, RandomBoarding
from passenger import Passenger
from plane import Plane


class Boarding:
    def __init__(self, plane=None):
        self.passenger_list = []
        self.boarding_process = None

        if plane:
            self.plane = plane
        else:
            print('Generating generic plane')
            self.plane = Plane(number_of_rows=30,
                               seats_per_row=6,
                               number_of_aisles=1,
                               doors=1,
                               overheads_per_row=2)

    def board(self):
        if not self.boarding_process:
            raise Exception('No boarding process specified')
        assert isinstance(self.boarding_process, BoardingProcess)
        self.boarding_process.board(self.plane, self.passenger_list)

    def print_description(self):
        print('\n\nWe have a plane with description :\n{}'.format(self.plane))
        print('We have {} passengers to board.'.format(len(self.passenger_list)))
        print('In total, we have {} items of luggage.'.format(self.luggage_count()))

        if self.passengers_fit_on_plane():
            print('OK to board, they will fit!')
        else:
            print('Need to find a bigger plane, too many passengers!')

        if self.luggage_fits_on_plane():
            print('OK to board, they will fit!')
        else:
            print('Need to find a bigger plane, too much luggage!')

    def generate_passengers(self, number_of_passengers):
        for i in range(0, number_of_passengers):
            self.passenger_list.append(Passenger())

    def passengers_fit_on_plane(self):
        number_of_passengers = len(self.passenger_list)
        seats_on_plane = self.plane.seats_on_plane()
        return seats_on_plane >= number_of_passengers

    def luggage_fits_on_plane(self):
        amount_of_luggage = self.luggage_count()
        overheads_on_plane = self.plane.overheads_on_plane()
        return overheads_on_plane >= amount_of_luggage

    def luggage_count(self):
        luggage_count = 0
        for p in self.passenger_list:
            assert isinstance(p, Passenger)
            luggage_count += len(p.lugagge_list)
        return luggage_count

    def assign_seats(self):
        seat_list = []
        for p in self.passenger_list:
            assert isinstance(p, Passenger)
            row = p.row_number = random.randint(0, self.plane.number_of_rows)
            seat = p.seat_number = random.randint(0, self.plane.seats_per_row)

            seat_list.append([row,seat])




if __name__ == '__main__':
    b = Boarding()

    b.print_description()

    b.generate_passengers(100)

    b.print_description()

    b.assign_seats()

    b.boarding_process = RandomBoarding()
    b.board()
