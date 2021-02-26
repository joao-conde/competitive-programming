import math
import random

from collections import defaultdict

def always_green(streets):
    counter = defaultdict(int)
    incoming_streets = defaultdict(list)
    for name, s in streets.items():
        counter[s["to"]]+=1
        incoming_streets[s["to"]].append(name)
    return [(intersection, incoming_streets[intersection][0]) for intersection, count in counter.items() if count==1]

def get_street_weights(cars):
    street_weights = defaultdict(int)
    for c in cars:
        for s in c["street_names"]:
            street_weights[s]+=1
    return street_weights

def get_street_weights_by_car_time(cars, sorted_arrivals):
    slowest_time = max(sorted_arrivals, key=lambda x: x[1])[1]
    sorted_arrivals_dict = dict(sorted_arrivals)
    street_weights = defaultdict(int)
    for i, c in enumerate(cars):
        for s in c["street_names"]:
            street_weights[s] += sorted_arrivals_dict[i]//slowest_time

def get_street_weights_distribution(street_weights, street_names):
    weight = street_weights[street_names[0]]
    for s in street_names[1:]:
        weight = math.gcd(weight, street_weights[s])
    distribution = []

    if weight== 0:
        for s in street_names:
            distribution.append((s, 1))
    else:
        for s in street_names:
            distribution.append((s, max(1, street_weights[s]//weight)))
    return distribution

def get_slow_cars(cars, streets, duration):
    def car_duration(car, streets):
        return sum([streets[street]["duration"] for street in car["street_names"]])

    car_durations = [(i, car_duration(car, streets)) for (i, car) in enumerate(cars)]
    useless_cars = [i for (i, c_duration) in enumerate(car_durations) if c_duration[1] > 1.0 * duration]
    return (len(useless_cars), useless_cars, car_durations)

def solve_meta(file, solution_func):
    data = parse_data(file)
    res = solution_func(file, *data)
    output_solution(file, res)
    return res

def solve_one(file, func):
    print("Solving %s..." % file)
    solve_meta(file, func)
    print("...Done")

def solve_all():
    A, B, C, D, E, F = ("a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt")
    problems = {
        A: solve,
        B: solve,
        C: solve,
        D: solve,
        E: solve,
        F: solve
    }
    for file, func in problems.items():
        solve_one(file, func)

def solve(current_file, *args):
    RES = [] # list of (ID of intersection, schedule: [street_name, duration]]

    duration, nintersections, nstreets, ncars, bonus, streets, cars, intersections = args
    ALL_SETS = set(range(0, nintersections))

    # remove useless cars (E only)
    if current_file == "e.txt":
        cars2 = []
        n_slow_cars, slow_cars, car_durations = get_slow_cars(cars, streets, duration)
        slow_cars = set(slow_cars)
        for i, car in enumerate(cars):
            if i not in slow_cars:
                cars2.append(car)
        print("Cars before %d, cars after %d (remove slow cars)" % (len(cars), len(cars2)))
        cars = cars2

    n_slow_cars, slow_cars, car_durations = get_slow_cars(cars, streets, duration) # refresh

    # always_green
    intersections_done = set()
    for intersection_id, incoming_street in always_green(streets):
        intersections_done.add(intersection_id)
        RES.append([intersection_id, [(incoming_street, duration)]])


    # sort cars by arrival time (fastest first): (index, duration)
    sorted_arrivals = sorted(car_durations, key=lambda x: x[1])

    street_weights = get_street_weights(cars)

    # not assigned
    not_assigned = ALL_SETS - intersections_done
    for intersection_id in not_assigned:
        in_streets = intersections[intersection_id]
        if current_file == "d.txt":
            RES.append([intersection_id, [(street, 1) for street in in_streets]])
        else:
            RES.append([intersection_id, get_street_weights_distribution(street_weights, in_streets)])

    return RES

def output_solution(fn, res):
    output = "out_%s" % fn
    with open(output, "w", encoding="utf-8") as file:
        file.write("%d\n" % len(res))
        for r in res:
            total_streets =  len(r[1])
            file.write("%d\n%d\n" % (r[0], total_streets)) # #incomingStreets
            for street, street_duration in r[1]:
                file.write("%s %d\n" % (street, street_duration))

def parse_data(fn):
    lines = read_file(fn).split("\n") # get all lines
    duration, nintersections, nstreets, ncars, bonus = mints(lines[0]) # map of ints
    intersections = defaultdict(list) # intersection_id -> [list of incoming streets]
    streets = {}
    for l in lines[1:nstreets+1]:
        _from, to, name, duration_street = l.split(" ")
        streets[name] = {"from": int(_from), "to": int(to), "name": name, "duration": int(duration_street)}
        intersections[int(to)].append(name)

    cars = []
    for l in lines[nstreets+1:nstreets+ncars+1]:
        parts = l.strip().split(" ")
        total_streets = int(parts[0])
        street_names = parts[1:]
        cars.append({"total_streets": total_streets, "street_names": street_names})

    return int(duration), int(nintersections), int(nstreets), int(ncars), bonus, streets, cars, intersections

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def mints(line):
    return map(int, line.strip().split(" "))

solve_all()
