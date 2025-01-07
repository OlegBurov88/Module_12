import unittest
import tests_12_3


testTS = unittest.TestSuite()

testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

STrunner = unittest.TextTestRunner(verbosity=2)
STrunner.run(testTS)