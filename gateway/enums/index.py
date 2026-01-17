from enum import Enum


class FundingAction(str, Enum):
    approve = "approve"
    reject = "reject"
