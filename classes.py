# Tworzenie nowego obiektu, wstęp do programowania obiektowego
class Person:  # nazwy klas wielką literą
    # pierwsza funkcja to konstruktor: funkcja wykonywana podczas tworzenia obiektu
    def __init__(self, xxx, yyy):
        self.name = xxx
        self.age = yyy

    # funkcja, żeby obiekt się przedstawił
    def tell_your_name(self):  # snake_case in function names
        print(f"My name is {self.name}")

    # funkcja, żeby obiekt powiedział, ile ma lat
    def define_age(self):
        print(f"My age is {self.age}")

    # funkcja zmiany imienia obiektu
    def change_name(self, zzz):
        self.name = zzz

    def addition(self, a, b):
        print(f"My name is {self.name}, I know that: {a} + {b} = {a + b}")


# wywołanie funkcji z klasy
# Person().print_name()

# wprowadzenie pierwszego obiektu w klasie Person, czyli wymagalnymi argumentami będzie określenie imienia i wieku
# karolina to nowy obiekt; klasa: Person; w nawiasie wymagane argumenty- tutaj jako input użytkownika
karolina = Person(input("Tell me your name: "), input("How old are you?: "))

# wywołanie obiektu karolina do powiedzenia z użyciem funkcji tell_your_name i define_age z klasy Person
karolina.tell_your_name()
karolina.define_age()

# wprowadzenie drugiego obiektu pawel
pawel = Person("Paweł", 30)
pawel.tell_your_name()
pawel.define_age()

# wywołanie obiektu karolina z funkcją change_name i argumentem, jaki funkcja ma przyjąć, czyli zmianą imienia na
# imię Joanna
karolina.change_name("Joanna")
karolina.tell_your_name()

# wywołanie obiektu karolina i pawel z klasy Person do sprawdzenia, że umieją wykonać dodawanie
karolina.addition(10, 20)
pawel.addition(10, 20)
