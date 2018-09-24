from passenger import Passenger


class BoardingProcess:
    def __init__(self):
        self.plane = None
        self.passenger_list = None

    def board(self, plane, passenger_list):
        raise NotImplementedError()


class SequentialBoarding(BoardingProcess):
    def board(self, plane, passenger_list):
        self.plane = plane
        self.passenger_list = passenger_list
        if not self.plane or not self.passenger_list:
            raise Exception('Need a plane and passenger list to board')

        print('\nBoarding with {} '.format(self))

        for p in passenger_list:
            assert isinstance(p, Passenger)
            if not p.seat_number:
                raise Exception('Need a seat number')
            if not p.row_number:
                raise Exception('Need a row number')

            print('Passenger trying to get to Row {} Seat {}'.format(p.row_number, p.seat_number))


class RandomBoarding(BoardingProcess):

    def __str__(self):
        return 'Random Boarding Process'

    def board(self, plane, passenger_list):
        self.plane = plane
        self.passenger_list = passenger_list
        if not self.plane or not self.passenger_list:
            raise Exception('Need a plane and passenger list to board')

        print('\nBoarding with {} '.format(self))

        self.assign_seats()

        for p in passenger_list:
            assert isinstance(p, Passenger)
            if not p.seat_number:
                raise Exception('Need a seat number')
            if not p.row_number:
                raise Exception('Need a row number')

            print('Passenger trying to get to Row {} Seat {}'.format(p.row_number, p.seat_number))

    def assign_seats(self):
        
        if not self.passenger_list:
            raise Exception('No passenger list to assign seats to.')


