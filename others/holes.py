def find_holes(frames_a, frames_b, n_frames):
    if len(frames_a) == 0 and len(frames_b) == 0:
        return [(0, n_frames)]

    events = []
    for s, e in frames_a + frames_b:
        events.append((s, 1))
        events.append((e, -1))

    events.sort()

    refs = 0
    holes = []

    t0, _ = events[0]
    if t0 > 0:
        holes.append((0, t0))

    hole_start = None
    for t, type in events:
        if refs == 0 and hole_start and hole_start != t:
            holes.append((hole_start, t))

        refs += type
        if refs == 0:
            hole_start = t

    tf, _ = events[-1]
    if tf < n_frames:
        holes.append((tf, n_frames))

    return holes


assert find_holes([], [], 10) == [(0, 10)]
assert find_holes([], [(10, 20), (40, 60), (110, 170)], 200) == [
    (0, 10),
    (20, 40),
    (60, 110),
    (170, 200),
]
assert find_holes([(10, 20), (40, 60), (110, 170)], [], 200) == [
    (0, 10),
    (20, 40),
    (60, 110),
    (170, 200),
]
assert find_holes([(10, 200)], [(10, 20), (40, 60), (110, 170)], 200) == [(0, 10)]
assert find_holes([(0, 10), (20, 30), (40, 50)], [(10, 20), (30, 40)], 50) == []
