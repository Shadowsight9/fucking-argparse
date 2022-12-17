import argparse
import unittest
from pathlib import Path

from fucking_argparse import gen_codes


class TestStringMethods(unittest.TestCase):
    def test_gen_codes(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--inductor", type=str, default="rule")
        parser.add_argument("--group_beam", type=bool, default=False)
        parser.add_argument("--mlm_training", type=bool, default=False)
        parser.add_argument("--bart_training", type=bool, default=False)
        parser.add_argument("--if_then", type=bool, default=False)
        parser.add_argument("--task", type=str, default="openrule155")
        gen_args = gen_codes(args=parser.parse_args())

        with open(Path(__file__).parent / "arguments.py") as file:
            self.assertEqual(gen_args, file.read())


if __name__ == "__main__":
    unittest.main()
