from dataclasses import dataclass
from pathlib import PosixPath
from torch import device
from torch.nn.modules.linear import Linear


@dataclass()
class Arguments:
    test_str: str = "rule"
    test_bool: bool = False
    test_int: int = 123
    test_float: float = 3.1
    test_complex: complex = 1 + 2j
    test_list: list = [1, 2.1, "hello", False]
    test_set: set = {False, 1, 2.1, "hello"}
    test_dict: dict = {"a": 1, "b": 2.1, "c": "hello", "d": False}
    test_path: PosixPath = PosixPath(".")
    test_device: device = device(type="cuda", index=0)
    test_module: Linear = Linear(in_features=1, out_features=2, bias=True)
