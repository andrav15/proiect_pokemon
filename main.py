from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie
def scriere_pokemon():
    while True:
        nume=input("Nume pokemon: ")
        tip=input("Tip pokemon(Foc/Apa/Pamant): ").capitalize()
        if tip!='Foc' and tip!='Apa' and tip!='Pamant':#verif tip
            print("Tipul introdus nu exista!")
            continue
        viata=int(input("Viata pokemon: "))
        putere_atac=int(input("Putere de atac pokemon: "))
        return Pokemon(nume,tip,viata,putere_atac)
def batalie():
    pokemoni_antrenor1=[]#lista goala cu pokemoni antrenor1
    for i in range(3):#3pokemoni dif
        print(f"Date pokemon {i + 1}:")
        pokemon=scriere_pokemon()#introducem date pok1
        pokemoni_antrenor1.append(pokemon)#facem lista cu pokemoni pt antrenor1
    pokemoni_antrenor2=[]#lista goala cu pokemoni antrenor2
    for i in range(3):
        print(f"Date pokemon {i + 1}:")
        pokemon=scriere_pokemon()
        pokemoni_antrenor2.append(pokemon)
    nume_antrenor1=input("\nNume antrenor1: ")#ad nume antrenor
    nume_antrenor2=input("Nume antrenor2: ")
    antrenor1=Antrenor(nume_antrenor1,pokemoni_antrenor1)
    antrenor2=Antrenor(nume_antrenor2,pokemoni_antrenor2)
    batalie=Batalie()
    batalie.lupta(antrenor1,antrenor2)
if __name__ == "__main__":
    batalie()
