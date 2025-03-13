class Kassapaate:
    EDULLINEN_HINTA = 240
    MAUKAS_HINTA = 400

    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= self.EDULLINEN_HINTA:
            self.kassassa_rahaa = self.kassassa_rahaa + self.EDULLINEN_HINTA
            self.edulliset += 1
            return (maksu - self.EDULLINEN_HINTA) / 100
        else:
            return maksu / 100

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= self.MAUKAS_HINTA:
            self.kassassa_rahaa = self.kassassa_rahaa + self.MAUKAS_HINTA
            self.maukkaat += 1
            return (maksu - self.MAUKAS_HINTA) / 100
        else:
            return maksu / 100
    

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= self.EDULLINEN_HINTA:
            kortti.ota_rahaa(self.EDULLINEN_HINTA)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= self.MAUKAS_HINTA:
            kortti.ota_rahaa(self.MAUKAS_HINTA)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return

    def kassassa_rahaa_euroina(self):
        return self.kassassa_rahaa / 100
