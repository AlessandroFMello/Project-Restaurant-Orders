class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        new_order = (customer, order, day)
        self.orders.append(new_order)

    def get_all_orders_from_customer(self, customer):
        all_orders_from_customer = dict()
        for order in self.orders:
            if order[0] == customer:
                if order[1] not in all_orders_from_customer:
                    all_orders_from_customer[order[1]] = 1
                else:
                    all_orders_from_customer[order[1]] += 1

        return all_orders_from_customer

    def get_most_ordered_dish_per_customer(self, customer):
        all_orders_from_customer = self.get_all_orders_from_customer(customer)

        quantity = 0
        most_ordered = ''
        for food in all_orders_from_customer:
            if all_orders_from_customer[food] > quantity:
                quantity = all_orders_from_customer[food]
                most_ordered = food

        return most_ordered

    def get_all_foods(self):
        all_foods = set()
        for order in self.orders:
            all_foods.add(order[1])

        return all_foods

    def get_never_ordered_per_customer(self, customer):
        all_foods = set(sorted(self.get_all_foods()))
        all_orders_from_customer = self.get_all_orders_from_customer(customer)

        for food in all_orders_from_customer:
            if food in all_foods:
                all_foods.remove(food)

        return all_foods

    def get_all_days(self):
        all_days = set()
        for order in self.orders:
            if order[2] not in all_days:
                all_days.add(order[2])

        return all_days

    def get_all_days_from_customer(self, customer):
        all_days_from_customer = dict()
        for order in self.orders:
            if order[0] == customer:
                if order[1] not in all_days_from_customer:
                    all_days_from_customer[order[2]] = True

        return all_days_from_customer

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(sorted(self.get_all_days()))
        all_days_for_customer = self.get_all_days_from_customer(customer)

        for day in all_days_for_customer:
            all_days.remove(day)

        return all_days

    def get_all_days_quantity(self):
        all_days = dict()
        for order in self.orders:
            if order[2] not in all_days:
                all_days[order[2]] = 1
            else:
                all_days[order[2]] += 1

        return all_days

    def get_busiest_day(self):
        all_days_with_quantity = self.get_all_days_quantity()

        most_visited_day = ''
        most_visited_times = 0
        for day, quantity in all_days_with_quantity.items():
            if quantity > most_visited_times:
                most_visited_times = quantity
                most_visited_day = day

        return most_visited_day

    def get_least_busy_day(self):
        all_days_with_quantity = self.get_all_days_quantity()
        least_visited_day = ''
        least_visited_times = 1000
        for day, quantity in all_days_with_quantity.items():
            if quantity < least_visited_times:
                least_visited_times = quantity
                least_visited_day = day

        return least_visited_day
