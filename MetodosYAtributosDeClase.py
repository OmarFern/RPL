class Persona:
    ultimo_dni = 0  # Atributo de clase

    def __init__(self):
        self.dni = self.ultimo_dni + 1  # Atributo de instancia
        Persona.aumentar_ultimo_dni()
        # self.ultimo_dni = self.ultimo_dni + 1

    @classmethod
    def aumentar_ultimo_dni(cls):
        cls.ultimo_dni = cls.ultimo_dni + 1

    def mostrar_dni(self):
        print(self.dni)

    def mostrar_ultimo_dni(self):
        print(self.ultimo_dni)


def main():
    nicolas = Persona()
    joaquin = Persona()
    # julia = Persona()

    # print("Mi nombre es Julia y mi dni es ", end="")
    # julia.mostrar_dni()

    print("Mi nombre es Nicolas y mi dni es ", end="")
    nicolas.mostrar_dni()

    print("Mi nombre es Joaquin y mi dni es ", end="")
    joaquin.mostrar_dni()

    print("Segun yo (Nicolas), el último dni es ", end="")
    nicolas.mostrar_ultimo_dni()

    print("Segun yo (Joaquin), el último dni es ", end="")
    joaquin.mostrar_ultimo_dni()

    print(f"Yo soy la clase Persona y el último dni es {Persona.ultimo_dni}")
    Persona.aumentar_ultimo_dni()
    print(f"Soy denuevo la clase persona y ahora el último dni es {Persona.ultimo_dni}")


main()
