class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)
    
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        
        seats = [['O' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seats

    def _is_valid_seat(self, row, col):
        return 0 <= row < self._rows and 0 <= col < self._cols

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        seats_available = self._seats[id]
        for seat in seats_to_book:
            row, col = seat
            if not self._is_valid_seat(row, col):
                print(f"Invalid seat: {seat}")
                continue
            if seats_available[row][col] == 'X':
                print(f"Seat {seat} is already booked.")
            else:
                seats_available[row][col] = 'X'
                print(f"Seat {seat} booked successfully.")

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show in self._show_list:
            print(show)

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for show {id}:")
        seats_available = self._seats[id]
        for i in range(self._rows):
            for j in range(self._cols):
                if seats_available[i][j] == 'O':
                    print(f"Seat {i}, {j}")


def main():
    hall1 = Hall(rows=5, cols=5, hall_no=1)
    hall1.entry_show(id='111', movie_name='Rajkumar', time='12:00 PM')
    hall1.entry_show(id='222', movie_name='Shonar Char', time='03:00 PM')
    hall1.entry_show(id='333', movie_name='Omar', time='06:00 PM')
    hall1.entry_show(id='444', movie_name='Jinn 2', time='09:00 PM')

    while True:
        print("\n1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. EXIT")
        option = input("Enter your option: ")

        if option == '1':
            hall1.view_show_list()
        elif option == '2':
            show_id = input("Enter the ID of the show: ")
            hall1.view_available_seats(show_id)
        elif option == '3':
            show_id = input("Enter the ID of the show: ")
            seats_to_book = []
            while True:
                seat = input("Enter seat (row,col) to book (or 'done' to finish): ")
                if seat.lower() == 'done':
                    break
                try:
                    row, col = map(int, seat.split(','))
                    seats_to_book.append((row, col))
                except ValueError:
                    print("Invalid input format. Please enter row,col.")
            hall1.book_seats(show_id, seats_to_book)
        elif option == '4':
            break
        else:
            print("Invalid option. Please select again.")


main()
