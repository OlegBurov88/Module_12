import runner, unittest
import runner_and_tournament as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner_ = runner.Runner('test')
        for _ in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner_ = runner.Runner('test')
        for _ in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = runner.Runner('test 1')
        runner_2 = runner.Runner('test 2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tour_name in cls.all_results:
            print({key: str(value) for key, value in cls.all_results[tour_name].items()})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        tour_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        results = tour_1.start()
        TournamentTest.all_results['tour_1'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        tour_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        results = tour_2.start()
        TournamentTest.all_results['tour_2'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        tour_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tour_3.start()
        TournamentTest.all_results['tour_3'] = results
        self.assertTrue(results[max(results.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
