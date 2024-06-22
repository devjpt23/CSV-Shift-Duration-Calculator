import unittest
import extractingDataFromFile

class TestingFunc(unittest.TestCase):     

    def test_shiftTime(self):
        self.assertEqual(extractingDataFromFile.calculatingDuration("14:00","7:00"),"7:00:00")
        self.assertEqual(extractingDataFromFile.calculatingDuration("07:00","14:00"),"7:00:00")

if __name__ == '__main__':
    unittest.main()
