import random

class ConcessionariaGenerator:
    def __init__(self):
        self.lettere = [chr(i) for i in range(65, 91)]  # Lettere dell'alfabeto
        self.numeri = [str(i) for i in range(10)]  # Numeri da 0 a 9
        self.marche_auto = ["Fiat", "Ford", "Toyota", "Volkswagen", "Renault"]
        self.marche_moto = ["Honda", "Yamaha", "Kawasaki", "Suzuki", "Ducati"]
        self.marche_camion = ["Iveco", "Mercedes-Benz", "Volvo", "Scania", "MAN"]

    def genera_targa(self):
        targa = ''.join(random.choices(self.lettere, k=2)) + ' ' + ''.join(random.choices(self.numeri, k=3)) + ' ' + ''.join(random.choices(self.lettere, k=2))
        return targa

    def genera_autoveicolo(self):
        targa = self.genera_targa()
        marca = random.choice(self.marche_auto)
        modello = marca + " " + random.choice(["Panda", "Focus", "Yaris", "Golf", "Clio"])
        n_posti = random.randint(2, 5)
        prezzo_base = round(random.uniform(8000, 30000), 2)
        numero_porte = random.randint(3, 5)
        return f'self.__concessionaria.add_autoveicolo("{targa}", "{marca}", "{modello}", {n_posti}, {prezzo_base}, {numero_porte})'

    def genera_motoveicolo(self):
        targa = self.genera_targa()
        marca = random.choice(self.marche_moto)
        modello = marca + " " + random.choice(["CBR", "YZF-R", "Ninja", "GSX-R", "Panigale"])
        n_posti = random.randint(1, 2)
        prezzo_base = round(random.uniform(3000, 15000), 2)
        cilindrata = random.randint(125, 1200)
        return f'self.__concessionaria.add_motoveicolo("{targa}", "{marca}", "{modello}", {n_posti}, {prezzo_base}, {cilindrata})'

    def genera_autocarro(self):
        targa = self.genera_targa()
        marca = random.choice(self.marche_camion)
        modello = marca + " " + random.choice(["Eurocargo", "Actros", "FH", "R-series", "TGX"])
        n_posti = 2
        prezzo_base = round(random.uniform(30000, 100000), 2)
        max_capacity = random.randint(500, 3000)
        return f'self.__concessionaria.add_autocarro("{targa}", "{marca}", "{modello}", {n_posti}, {prezzo_base}, {max_capacity})'

    def genera_istruzioni(self, num_veicoli=20):
        istruzioni = []
        for _ in range(num_veicoli):
            tipo_veicolo = random.choice(['auto', 'moto', 'camion'])
            if tipo_veicolo == 'auto':
                istruzioni.append(self.genera_autoveicolo())
            elif tipo_veicolo == 'moto':
                istruzioni.append(self.genera_motoveicolo())
            else:
                istruzioni.append(self.genera_autocarro())
        return istruzioni

# Utilizzo della classe per generare istruzioni
concessionaria_generator = ConcessionariaGenerator()
istruzioni = concessionaria_generator.genera_istruzioni(num_veicoli=20)
for istruzione in istruzioni:
    print(istruzione)
