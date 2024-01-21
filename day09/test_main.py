import unittest

import main


class TestMain(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(main.solve("ADVENT"), len("ADVENT"))
        self.assertEqual(main.solve("A(1x5)BC"), len("ABBBBBC"))
        self.assertEqual(main.solve("(3x3)XYZ"), len("XYZXYZXYZ"))
        self.assertEqual(main.solve("A(2x2)BCD(2x2)EFG"), len("ABCBCDEFEFG"))
        self.assertEqual(main.solve("(6x1)(1x3)A"), len("(1x3)A"))
        self.assertEqual(main.solve("X(8x2)(3x3)ABCY"), len("X(3x3)ABC(3x3)ABCY"))

        self.assertEqual(
            main.solve("X(8x2)(3x3)ABCY", True), len("XABCABCABCABCABCABCY")
        )
        self.assertEqual(main.solve("(27x12)(20x12)(13x14)(7x10)(1x12)A", True), 241920)
        self.assertEqual(
            main.solve(
                "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", True
            ),
            445,
        )


if __name__ == "__main__":
    unittest.main()
