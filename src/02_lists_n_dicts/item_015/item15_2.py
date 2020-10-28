# - open PowerShell in admin mode
# - install mypy globally by running this command in PowerShell: pip install mypy
# - terminate existing terminals and launch a new one in VS Code
# - make sure mypy command is available in the new launched terminal
# - run the following command in the terminal to check the type issues
#   mypy --strict item15_2.py
# - the above command performs type checking, you still can run the python file
#   python item15_2.py


from collections.abc import MutableMapping
from typing import Dict, MutableMapping, Iterator

# use type annotation


def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    # type-checking error. not sure how to fix it
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class SortedDict(MutableMapping[str, int]):
    def __init__(self) -> None:
        self.data: Dict[str, int] = {}

    def __getitem__(self, key: str) -> int:
        return self.data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __iter__(self) -> Iterator[str]:
        keys = list(self.data.keys())
        keys.sort()  # order by key ascending; deviate from insertion order
        for key in keys:
            yield key

    def __len__(self) -> int:
        return len(self.data)


votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863
}

sorted_ranks = SortedDict()
#  "populate_ranks" has incompatible type "SortedDict"; expected "Dict[str, int]"
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
# "get_winner" has incompatible type "SortedDict"; expected "Dict[str, int]"
winner = get_winner(sorted_ranks)
print(winner)
