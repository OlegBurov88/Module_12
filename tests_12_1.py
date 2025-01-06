import runner, unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_ = runner.Runner('test')
        for _ in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)

    def test_run(self):
        runner_ = runner.Runner('test')
        for _ in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        runner_1 = runner.Runner('test 1')
        runner_2 = runner.Runner('test 2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
