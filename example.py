# Полиморфизм и doctyping


class WildDuck:
    def quack(slrf) -> str:
        return "Quack!!!!!!!!!"

    def some_decoy_method(self):
        pass



class Decoy:
    def quack(self) -> str:
        return "*False quack"
    
    def some_decoy_method(self):
        pass



def actions(value):
    print(value.quack())