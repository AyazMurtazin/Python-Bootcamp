from random import randint


def turrets_generator():
    a = [0, 0, 0, 0, 0]
    for i in range(100):
        a[randint(0, 4)] += 1

    def shoot():
        print("shoot")

    def search():
        print("search")

    def talk():
        print("talk")

    turret = {
        'neuroticism': a[0],
        'openness': a[1],
        'conscientiousness': a[2],
        'extraversion': a[3],
        'agreeableness': a[4],
        'shoot': shoot,
        'search': search,
        'talk': talk
    }
    return type('Turret', (object,), turret, )


turret = turrets_generator()
print(type(turret))

turret.shoot()
turret.search()
turret.talk()

print(turret.neuroticism)
print(turret.openness)
print(turret.conscientiousness)
print(turret.extraversion)
print(turret.agreeableness)
