# Fucking Argparse
A dataclass generate library for Namespace object generated by argparse

## Usage 
```python
import argparse
from fucking_argparse import gen_codes
parser = argparse.ArgumentParser()
parser.add_argument("--inductor", type=str, default="rule")
parser.add_argument("--group_beam", type=bool, default=False)
parser.add_argument("--mlm_training", type=bool, default=False)
parser.add_argument("--bart_training", type=bool, default=False)
parser.add_argument("--if_then", type=bool, default=False)
parser.add_argument("--task", type=str, default="openrule155")

gen_codes(args=parser.parse_args(), file_path="./arguments.py")

  
```

## Test

```bash
cd tests
python -m unittest
```