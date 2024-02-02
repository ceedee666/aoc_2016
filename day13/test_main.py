import unittest

import main


class TestMain(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            main.solve((7, 4), favorite_num=10),
            11,
            "The minimal number of steps should be 11",
        )


if __name__ == "__main__":
    unittest.main()
