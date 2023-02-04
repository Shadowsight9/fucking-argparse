import argparse
import unittest
from pathlib import Path

import torch

from fucking_argparse import gen_codes


class TestGenMethods(unittest.TestCase):
    def test_gen_codes(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--test_str", type=str, default="rule")
        parser.add_argument("--test_bool", type=bool, default=False)
        parser.add_argument("--test_int", type=int, default=123)
        parser.add_argument("--test_float", type=float, default=3.1)
        parser.add_argument("--test_complex", type=complex, default=1 + 2j)
        parser.add_argument("--test_list", type=list, default=[1, 2.1, "hello", False])
        parser.add_argument(
            "--test_set", type=complex, default={1, 2.1, "hello", False}
        )
        parser.add_argument(
            "--test_dict",
            type=complex,
            default={"a": 1, "b": 2.1, "c": "hello", "d": False},
        )
        parser.add_argument("--test_path", type=Path, default=Path("."))
        parser.add_argument("--test_device", type=torch.device, default=torch.device(0))
        parser.add_argument(
            "--test_module", type=torch.nn.Module, default=torch.nn.Linear(1, 2)
        )
        # gen_codes(args=parser.parse_args(), file_path="./arguments.py", exist_ok=True)
        gen_args = gen_codes(args=parser.parse_args(), class_name="Arguments")

        with open(Path(__file__).parent / "arguments.py") as file:
            self.assertEqual(gen_args, file.read())


if __name__ == "__main__":
    unittest.main()
