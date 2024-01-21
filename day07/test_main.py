import unittest

import main

test_string = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

test_string_2 = "rxpusykufgqujfe[rypwoorxdemxffui]cvvcufcqmxoxcphp[witynplrfvquduiot]vcysdcsowcxhphp[gctucefriclxaonpwe]jdprpdvpeumrhokrcjt"


test_string_3 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""


class TestMain(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(main.solve(test_string.split("\n"))[0], 2)
        self.assertEqual(main.solve([test_string_2])[0], 1)

        self.assertEqual(main.solve(test_string_3.split("\n"))[1], 3)


if __name__ == "__main__":
    unittest.main()
