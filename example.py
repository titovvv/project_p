# полиморфизм и doc typing




from typing import Protocol




class Quackable(Protocol):
    def quack(self) -> str: ...



class WildDuck:
    def quack(self) -> str:
        return "Quack!"
    
    def some_duck_method(self):
        pass



class Decoy:
    def quack(self) -> str:
        return "*False* quack!"
    

    def some_decoy_method(self):
        pass




class RubberDuck:
    def quack(self) -> str:
        return "Squezeeeee!"


# def action(value: WildDuck | Decoy | RubberDuck):
#     print(value.quack())


def action(value: Quackable):
    print(value.quack())



# -------------------------------- нам нужно:
# 1. подсказки IDE
# 2. удобство, писание в сигнатуре
# 3. сохранить гибкость(полиморфизм) и doc typing
# 4. лаконично написано



# должна быть реализована правильная абстракция