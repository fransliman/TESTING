import unittest

# Fungsi sederhana yang akan diuji
def tambah(a, b):
    return a + b

# Kelas tes untuk menguji fungsi tambah
class TestTambah(unittest.TestCase):
    def test_tambah_angka_positif(self):
        self.assertEqual(tambah(3, 5), 8)  # Memeriksa penambahan angka positif

    def test_tambah_angka_negatif(self):
        self.assertEqual(tambah(-2, 2), 0)  # Memeriksa penambahan angka negatif

    def test_tambah_nol(self):
        self.assertEqual(tambah(0, 7), 7)  # Memeriksa penambahan nol

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestTambah))
    if result.wasSuccessful():
        print("Semua tes berhasil!")