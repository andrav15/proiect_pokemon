class Antrenor:
    def __init__(self,nume,pokemoni):
        self.nume=nume
        self.pokemoni=pokemoni
    def alege_pokemon(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                print(f"Primul pokemon din cei care sunt in viata este: {pokemon.nume}")
                return pokemon
        print(f"Nu exista pokemoni vii")
        return None
    def are_pokemoni_vii(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return True
            else:
                return False
        return None