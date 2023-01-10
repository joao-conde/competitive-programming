from collections import defaultdict


def most_reserved(bookings):
    in_use = set()
    check_ins = defaultdict(lambda: 0)

    for booking in bookings:
        check_in = booking[0] == "+"
        room = booking[1:]

        if check_in and room not in in_use:
            check_ins[room] += 1
            in_use.add(room)

        if not check_in:
            in_use.remove(room)

    result, reservations = None, 0
    for (room, count) in check_ins.items():

        if count > reservations:
            reservations = count
            result = room

        if count == reservations and (result == None or room < result):
            reservations = count
            result = room

    return result


assert most_reserved(["+3A", "-3A", "+3A", "+4C"]) == "3A"
assert most_reserved(["+3A", "+3A", "+3A", "+4C", "-4C", "+4C"]) == "4C"
assert most_reserved(["+3C", "+3A"]) == "3A"
assert most_reserved(["+6A", "+3Z"]) == "3Z"
