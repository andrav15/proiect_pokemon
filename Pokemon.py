class Pokemon:
    def __init__(self,nume,tip,viata,putere_atac):
        self.nume=nume
        self.tip=self.tip(tip)
        self.viata=viata
        self.putere_atac=putere_atac

    def tip(self,tip):
        while tip!='Foc' and tip!='Apa' and tip!='Pamant':
            print(f"Nu exista tipul acesta!")
            tip=input("Introduceti un tip valid: ")
        self.tip=tip
        return self.tip


    def ataca(self,pokemon):
        if self.viata!=0 and pokemon.viata!=0:
            pokemon.viata -= self.putere_atac
    def este_viu(self):
        if self.viata>0:
            return True
        else:
            return False
