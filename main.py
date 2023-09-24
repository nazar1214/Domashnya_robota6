class SmakMoroziva:
    def __init__(self, smak):
        self.smak = smak

class Morozivo:
    def __init__(self):
        self.smaki = []

    def dodati_smak(self, smak):
        self.smaki.append(smak)

    def vybrati_smaki(self, kilkist):
        vybrani_smaki = self.smaki[:kilkist]
        return vybrani_smaki

smak1 = SmakMoroziva("ванілний")
smak2 = SmakMoroziva("полуничний")
smak3 = SmakMoroziva("шоколадний")
smak4 = SmakMoroziva("лимоний")

morozivo = Morozivo()
morozivo.dodati_smak(smak1)
morozivo.dodati_smak(smak2)
morozivo.dodati_smak(smak3)
morozivo.dodati_smak(smak4)


vybrani_smaki = morozivo.vybrati_smaki(int(input("виберіть Виберіть скільки кульок хочете(1-4): "))) 

if vybrani_smaki:
    print("")
    for smak in vybrani_smaki:
        print(smak.smak)
