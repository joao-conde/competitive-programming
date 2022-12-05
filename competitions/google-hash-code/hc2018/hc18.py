class Car:
    def __init__(self):
        self.pos = [0, 0]
        self.occupied = False
        self.origin = False
        self.rides = []
        self.history = []


class Ride:
    def __init__(self, id, start, finish, early_start, latest_start):
        self.id = id
        self.start = start
        self.finish = finish
        self.early_start = early_start
        self.latest_start = latest_start
        self.on_road = False
        self.completed = False


def parse_input(filename, num_cars, num_rides, ticks):
    file = open(filename, "r")
    lines = file.readlines()

    first_line = lines[0].split()
    first_line = [int(x) for x in first_line]

    num_cars = first_line[2]
    num_rides = first_line[3]
    ticks = first_line[5]

    for i, line in enumerate(lines):
        if i == 0:
            continue
        line = line.split()
        int_line = [int(x) for x in line]
        rides.append(
            Ride(
                i - 1,
                [int_line[0], int_line[1]],
                [int_line[2], int_line[3]],
                int_line[4],
                int_line[5],
            )
        )

    return [num_cars, num_rides, ticks]


def generate_cars(num_cars):
    return [Car() in range(num_cars)]


def run_clock(ticks):
    for _ in range(ticks):
        assign_ride_to_car(cars, rides)
        place_on_origin(cars)
        make_trip(cars)
        check_if_completed(cars)


def assign_ride_to_car(cars, rides):
    for ride in rides:
        if ride.on_road or ride.completed:
            continue

        distances = [calculate_car_distance(car, ride) for car in cars]
        min_car = distances.index(min(distances))
        cars[min_car].rides.append(ride)
        cars[min_car].occupied = True
        ride.on_road = True


def calculate_car_distance(car, ride):
    if car.occupied:
        step_1 = calculate_distance(car.pos, car.rides[0].finish)
        step_2 = calculate_distance(car.rides[0].finish, ride.start)
        return step_1 + step_2
    return calculate_distance(car.pos, ride.start)


def calculate_distance(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return dx + dy


def place_on_origin(cars):
    for car in cars:
        if car.origin or len(car.rides) == 0:
            continue

        if car.pos[0] != car.rides[0].start[0]:
            if car.pos[0] < car.rides[0].start[0]:
                car.pos[0] += 1

            elif car.pos[0] > car.rides[0].start[0]:
                car.pos[0] -= 1

        elif car.pos == car.rides[0].start:
            car.origin = True

        else:
            if car.pos[1] < car.rides[0].start[1]:
                car.pos[1] += 1

            elif car.pos[1] > car.rides[0].start[1]:
                car.pos[1] -= 1


def make_trip(cars):
    for car in cars:
        if not car.origin or len(car.rides) == 0:
            continue

        if car.pos[0] != car.rides[0].finish[0]:
            if car.pos[0] < car.rides[0].finish[0]:
                car.pos[0] += 1

            elif car.pos[0] > car.rides[0].finish[0]:
                car.pos[0] -= 1

        else:
            if car.pos[1] < car.rides[0].finish[1]:
                car.pos[1] += 1

            elif car.pos[1] > car.rides[0].finish[1]:
                car.pos[1] -= 1


def check_if_completed(cars):
    for car in cars:

        if car.origin and car.pos == car.rides[0].finish:
            car.occupied = False
            car.origin = False
            car.rides[0].completed = True
            car.history.append(car.rides[0].id)

            if len(car.rides) != 1:
                car.rides = car.rides[1 - len(car.rides) :]
            else:
                car.rides = []


def show_results(output_path):
    file = open(output_path, "a")
    for car in cars:
        file.write(str(len(car.history)))
        file.write(" ")
        file.write(" ".join(str(x) for x in car.history))
        file.write("\n")


if __name__ == "__main__":
    input_path = "a.in"
    output_path = "a.out"
    rides = []
    num_cars = num_rides = ticks = 0
    parse_results = parse_input(input_path, num_cars, num_rides, ticks)
    num_cars = parse_results[0]
    num_rides = parse_results[1]
    ticks = parse_results[2]
    cars = generate_cars(num_cars)
    run_clock(ticks)
    show_results(output_path)
