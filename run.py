from example import action, WildDuck, Decoy



if __name__ == '__main__':
    duck = WildDuck()
    action(duck)
    decoy = Decoy()
    action(Decoy)

    action("Not a duck")
    action(None)