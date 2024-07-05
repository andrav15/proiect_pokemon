class Batalie:
    def lupta(self, antrenor1, antrenor2):
        while antrenor1.are_pokemoni_vii() and antrenor2.are_pokemoni_vii():
            p1=antrenor1.alege_pokemon()
            p2=antrenor2.alege_pokemon()
            if p1 != None and p2 != None:
                print(f"{antrenor1.nume} il alege pe {p1.nume}. {antrenor2.nume} il alege pe {p2.nume}")
                while p1.este_viu() and p2.este_viu():
                    p1.ataca(p2)
                    if p2.este_viu():
                        p2.ataca(p1)

                if not p1.este_viu():
                    print(f"{p1.nume} a fost invins!")
                    antrenor1.pokemoni.remove(p1)
                if not p2.este_viu():
                    print(f"{p2.nume} a fost invins!")
                    antrenor2.pokemoni.remove(p2)

            else:
                print("Antrenorii nu au pokemoni in viata!")
                return None
        if antrenor1.are_pokemoni_vii():
            print(f"{antrenor1.nume} a castigat!")
        elif antrenor2.are_pokemoni_vii():
            print(f"{antrenor2.nume} a castigat!")
        else:
            print("Nu a castigat nimeni!")
