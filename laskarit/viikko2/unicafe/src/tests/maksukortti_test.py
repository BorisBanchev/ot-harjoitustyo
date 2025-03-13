import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        uusi_saldo = self.maksukortti.saldo_euroina()

        self.assertEqual(uusi_saldo, 12.0)
    
    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        uusi_saldo = self.maksukortti.saldo_euroina()
        
        self.assertEqual(uusi_saldo, 8.0)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        uusi_saldo = self.maksukortti.saldo_euroina()
        
        self.assertEqual(uusi_saldo, 10.0)
    
    def test_palauttaa_true_jos_tarpeeksi_saldoa_muuten_false(self):
        kortti_1 = Maksukortti(600)
        kortti_2 = Maksukortti(1500)
        
        # saldoa ei ole tarpeeksi kortti1 palauttaa False
        saldoa_kortissa_1 = kortti_1.ota_rahaa(800)
        self.assertEqual(saldoa_kortissa_1, False)
        
        # saldoa on tarpeeksi kortti2 palauttaa True
        saldoa_kortissa_2 = kortti_2.ota_rahaa(1000)
        self.assertEqual(saldoa_kortissa_2, True)

    def test_maksukortin_tulostus_antaa_oikean_merkkijonoesityksen(self):
        merkkijonoesitys = self.maksukortti.__str__()
        self.assertEqual(merkkijonoesitys, "Kortilla on rahaa 10.00 euroa")