# class MyList:
#     def __init__(self):
#         self._list = []

#     def append(self, item):
#         self._list.append(item)

#     def remove(self, item):
#         self._list.remove(item)

#     def pop(self, index=None):
#         return self._list.pop(index)

#     def count(self, item):
#         return self._list.count(item)

#     def sort(self, key=None, reverse=False):
#         self._list.sort(key=key, reverse=reverse)

#     def reverse(self):
#         self._list.reverse()

#     def __getitem__(self, index):
#         return self._list[index]

#     def __setitem__(self, index, value):
#         self._list[index] = value

#     def __delitem__(self, index):
#         del self._list[index]

#     def __len__(self):
#         return len(self._list)

#     def __str__(self):
#         return str(self._list)

#     def __repr__(self):
#         return repr(self._list)

# list1 = MyList()
# list1.append(3)
# list1.remove(3)
# print(list1)




class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.reservations = {}

    def make_reservation(self, name, tables, date):
        if date not in self.reservations:
            if tables <= self.tables:
                self.reservations[date] = self.tables - tables
                print(f"Reservation made for {name} at {date}.")
            else:
                print("No seats available.")
        else:
            if tables <= self.reservations[date]:
                self.reservations[date] -= tables
                print(f"Reservation made for {name} at {date}.")
            else:
                print("No seats available.")

    def order_food(self, *args):
        print(f"Order with {', '.join(args)} placed!։")


class FastFoodRestaurant(Restaurant):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_reservation(self, *args, **kwargs):
        print("We do not take reservations.")


restaurant = Restaurant('Paradise', 5)
restaurant.make_reservation('Anna', 2, '2024-05-06-19')
restaurant.make_reservation('Ashot', 3, '2024-05-07-19')
restaurant.make_reservation('Mary', 1, '2024-05-07-19')
restaurant.make_reservation('Lilit', 2, '2024-05-07-19')
fast_food = FastFoodRestaurant('Burger World')
fast_food.make_reservation('John', 2, '2023-10-24-19')
fast_food.order_food('Burger', 'Soda', 'Fries')

