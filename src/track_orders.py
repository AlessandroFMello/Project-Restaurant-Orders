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
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
