from dataclasses import dataclass


@dataclass()
class Arguments:
    inductor: str = "rule"
    group_beam: bool = False
    mlm_training: bool = False
    bart_training: bool = False
    if_then: bool = False
    task: str = "openrule155"
