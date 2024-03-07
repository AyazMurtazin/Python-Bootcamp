import itertools


def fix_wiring(cables, sockets: list, plugs: list):
    return [f"plug {i} into {j} using {k}" if k else f"weld {i} to {j}  without plug"
            for i, j, k in itertools.zip_longest([i for i in cables if type(i) == str],
                                                 [i for i in sockets if type(i) == str],
                                                 [i for i in plugs if type(i) == str])
            if all([i, j])]


if __name__ == "__main__":
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    print("example 1")
    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    print("example 2")
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
