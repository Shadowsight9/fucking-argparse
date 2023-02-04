"""Core package for code generate"""
import builtins
import importlib
import re
from argparse import Namespace
from collections import defaultdict
from pathlib import Path
from typing import Any, DefaultDict, Optional, overload

CODE_TEMPLATE = """

@dataclass()
class """


@overload
def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
    file_path: str | Path = "./arguments.py",
    exist_ok: bool = False,
    autoformat: bool = True,
) -> None:
    ...


@overload
def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
    autoformat: bool = True,
) -> str:
    ...


def gen_codes(
    args: Namespace,
    class_name: str = "Arguments",
    file_path: Optional[str | Path] = None,
    exist_ok: bool = False,
    tabsize: int = 4,
    autoformat: bool = True,
):
    """use to generate dataclass codes"""
    code_str = CODE_TEMPLATE
    code_str += f"{class_name}:\n"
    module_list: list[list[str]] = []
    module_list.append(["dataclasses", "dataclass"])
    for key, value in args.__dict__.items():
        line_str, module_dir = type_formatter(key, value, tabsize=tabsize)
        code_str += line_str
        module_list.append(module_dir)
    code_str = import_formatter(module_list) + code_str

    if autoformat:
        if importlib.util.find_spec("black") is not None:
            import black  # pylint: disable=C0415

            code_str = black.format_str(code_str, mode=black.Mode())

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


def type_formatter(key: str, value: Any, tabsize: int = 4):
    value_type = type(value)
    tab_str = " " * tabsize
    code_line = f"{tab_str}{key}: {value_type.__name__} = "
    if value_type is str:
        code_line += f'"{value}"\n'
    else:
        code_line += f"{repr(value)}\n"

    matches = re.findall(r"class '(.*)'", str(value_type))
    module_dir: list[str] = matches[0].split(".")
    return code_line, module_dir


def import_formatter(module_list: list[list[str]]):
    import_dict: DefaultDict[str] = defaultdict(set)
    for item in module_list:
        prefix_str = ".".join(item[:-1])
        import_dict[prefix_str].add(item[-1])
    import_str = ""

    for key, values in import_dict.items():
        if key == "":
            values = [val for val in values if val not in dir(builtins)]
            for val in values:
                import_str += f"import {val}\n"
        else:
            import_str += f"from {key} import {', '.join(values)}\n"

    return import_str
