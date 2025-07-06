from example import action, WildDuck, Decoy, RubberDuck



if __name__ == '__main__':
    duck = WildDuck()
    action(duck)
    decoy = Decoy()
    action(Decoy)
    duck = RubberDuck()
    action(duck)

    action("Not a duck")
    action(None)