import unittest

import main

test_string = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""


class TestMain(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(main.solve(test_string.split("\n")), 1514)


if __name__ == "__main__":
    unittest.main()
