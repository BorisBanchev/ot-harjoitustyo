import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10000)

    def test_luodussa_kassassa_oikea_saldo_ja_nolla_lounasta_myyty(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        lounaita_yhteensa = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaita_yhteensa, 0)
    
    def test_jos_kateismaksu_riittava_kassan_saldo_kasvaa_edullisen_lounaan_hinnalla_ja_vaihtoraha_on_oikea(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        kassan_uusi_saldo = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(vaihtoraha, 0.1)
        self.assertEqual(kassan_uusi_saldo, 1002.4)
    
    def test_jos_kateismaksu_riittava_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        edullisia = self.kassapaate.edulliset
        self.kassapaate.syo_maukkaasti_kateisella(500)
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(edullisia, 1)
        self.assertEqual(maukkaita, 1)
    
    def test_jos_kateismaksu_ei_riittava_saldo_ei_muutu_rahat_takaisin_lounaiden_maara_sama(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        vaihtoraha2 = self.kassapaate.syo_maukkaasti_kateisella(300)
        kassan_saldo = self.kassapaate.kassassa_rahaa_euroina()
        lounaita = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(vaihtoraha, 2.0)
        self.assertEqual(vaihtoraha2, 3.0)
        self.assertEqual(kassan_saldo, 1000)
        self.assertEqual(lounaita, 0)
    
    def test_jos_kortilla_rahaa_veloitetaan_edullinen_lounas_ja_palautetaan_true(self):
        maksu_onnistunut = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        kortin_saldo_maksun_jalkeen = self.maksukortti.saldo_euroina()
        
        self.assertEqual(maksu_onnistunut, True)
        self.assertEqual(kortin_saldo_maksun_jalkeen, 97.6)

    def test_jos_kortilla_rahaa_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        lounaita = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaita, 2)
    
    def test_jos_kortilla_ei_rahaa_kortin_saldo_sama_lounaiden_maara_sama_palautetaan_false(self):
        maksukortti = Maksukortti(100)
        maksu1_onnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        maksu2_onnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        lounaita_yhteensa = self.kassapaate.edulliset + self.kassapaate.maukkaat
        kortin_saldo = maksukortti.saldo_euroina()

        self.assertEqual(maksu1_onnistui, False)
        self.assertEqual(maksu2_onnistui, False)
        self.assertEqual(lounaita_yhteensa, 0)
        self.assertEqual(kortin_saldo, 1)
    def test_kassan_saldo_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        kassan_saldo = self.kassapaate.kassassa_rahaa_euroina()
        
        self.assertEqual(kassan_saldo, 1000)

    def test_kortille_ladattaessa_rahaa_kortin_saldo_nousee_kassan_saldo_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        kortin_uusi_saldo = self.maksukortti.saldo_euroina()
        kassan_uusi_saldo = self.kassapaate.kassassa_rahaa_euroina()
        
        self.assertEqual(kortin_uusi_saldo, 101)
        self.assertEqual(kassan_uusi_saldo, 1001)

    def test_ladattaessa_negatiivista_saldoa_kortille_kortin_ja_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -300)
        kortin_saldo = self.maksukortti.saldo_euroina()
        kassan_saldo = self.kassapaate.kassassa_rahaa_euroina()
        
        self.assertEqual(kortin_saldo, 100)
        self.assertEqual(kassan_saldo, 1000)