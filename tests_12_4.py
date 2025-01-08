import logging, unittest
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_ = rt.Runner('test', -5)
            for _ in range(10):
                runner_.walk()
            self.assertEqual(runner_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_ = rt.Runner(5)
            for _ in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner_1 = rt.Runner('test 1')
        runner_2 = rt.Runner('test 2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')
