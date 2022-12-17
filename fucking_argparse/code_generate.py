"""Core package for code generate"""
from argparse import Namespace
from pathlib import Path
from typing import Optional, overload

CODE_TEMPLATE = """from dataclasses import dataclass


@dataclass()
class """


@overload
def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
    file_path: str | Path = "./arguments.py",
    exist_ok: bool = False,
) -> None:
    ...


@overload
def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
) -> str:
    ...


def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
    file_path: Optional[str | Path] = None,
    exist_ok: bool = False,
    tabszie: int = 4,
):
    """use to generate dataclass codes"""
    code_str = CODE_TEMPLATE
    code_str += f"{class_name}:\n"
    tab_str = " " * tabszie
    for key, value in args.__dict__.items():
        value_type = type(value)
        code_str += f"{tab_str}{key}: {value_type.__name__} = "
        if value_type is str:
            code_str += f'"{value}"\n'
        else:
            code_str += f"{value}\n"

    if file_path is None:
        return code_str

    if isinstance(file_path, str):
        file_path = Path(file_path)
    elif isinstance(file_path, Path):
        raise TypeError("Unknown type for output path!")

    if not exist_ok and file_path.is_file():
        raise FileExistsError("file is already exist! set exist_ok=True")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code_str)
