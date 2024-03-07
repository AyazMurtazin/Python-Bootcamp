def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = {"gold_ingots": 0}
    try:
        new_purse["gold_ingots"] = purse["gold_ingots"] + 1
    except KeyError:
        new_purse["gold_ingots"] = 1
    return new_purse


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = {"gold_ingots": 0}
    try:
        if (_ := purse["gold_ingots"] - 1) >= 0:
            new_purse["gold_ingots"] = _
    except KeyError:
        pass
    return new_purse


def empty(purse: dict[str, int]) -> dict[str, int]:
    new_purse = {"gold_ingots": 0}
    return new_purse


if __name__ == "__main__":
    start_purse = {"gold_ingots": 1, "stones": 1}
    print("---test_add---")
    print("start_purse:", start_purse)
    print("add_ignot_result:", add_ingot(start_purse))
    print("end_purse:", start_purse)

    print("---test_get---")
    print("start_purse:", start_purse)
    print("add_ignot_result:", get_ingot(start_purse))
    print("end_purse:", start_purse)

    print("---test_empty---")
    print("start_purse:", start_purse)
    print("empty_result:", empty(start_purse))
    print("end_purse:", start_purse)

    start_purse["gold_ingots"] = 0

    print("---test_get_from_0---")
    print("start_purse:", start_purse)
    print("get_ignot_result:", get_ingot(start_purse))
    print("end_purse:", start_purse)

    print("---test_add_to_0---")
    print("start_purse:", start_purse)
    print("add_ignot_result:", add_ingot(start_purse))
    print("end_purse:", start_purse)

    start_purse.pop("gold_ingots")

    print("---test_add_to_no_key---")
    print("start_purse:", start_purse)
    print("add_ignot_result:", add_ingot(start_purse))
    print("end_purse:", start_purse)

    print("---test_get_from_no_key---")
    print("start_purse:", start_purse)
    print("get_ignot_result:", get_ingot(start_purse))
    print("end_purse:", start_purse)
