class Key:
    def __init__(self):
        self.pessphrase = "zax2rulez"

    def __str__(self):
        return "GeneralTsoKeycard"

    def __len__(self):
        return 1337

    def __gt__(self, other):
        return True if other == 9000 else False

    def __getitem__(self, item):
        return 3 if item == 404 else 0


if __name__ == "__main__":
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.pessphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
