def split_booty(*args: dict[str, int]):
    purses_cnt = len(args)
    summ = sum(i["gold_ingots"] for i in args if "gold_ingots" in i)
    return tuple(
        {"gold_ingots": (summ + i) // 3} for i in reversed(range(3)))


if __name__ == "__main__":
    normal_purse = {"gold_ingots": 2}
    surplus_purse = {"gold_ingots": 4, "stones": 1}
    zero_ingots_purse = {"gold_ingots": 0, "stones": 1}
    no_ingots_purse = {"stones": 1}
    print("4 normal purses:", split_booty(normal_purse, normal_purse, normal_purse, normal_purse))
    print("3 surplus purses:", split_booty(surplus_purse, surplus_purse, surplus_purse))
    print("2 zero ingots purses:", split_booty(zero_ingots_purse, zero_ingots_purse))
    print("3 no_ingots_purse purses:", split_booty(no_ingots_purse, no_ingots_purse, no_ingots_purse))
    print("4 all ingot types purses:", split_booty(normal_purse, no_ingots_purse, zero_ingots_purse, surplus_purse))
