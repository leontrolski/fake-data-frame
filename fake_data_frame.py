from typing import Any, Dict, List

class FakeSeries:
    def __init__(self, name: str, data: Dict[int, Any]):
        self.name = name
        self.data = data

    # handle *
    def __mul__(self, other: int) -> 'FakeSeries':
        return FakeSeries(
            self.name,
            {i: v * other for i, v in self.data.items()},
        )

    # handle >
    def __gt__(self, other: int) -> 'FakeSeries':
        return FakeSeries(
            self.name,
            {i: v > other for i, v in self.data.items()},
        )

    # handle []
    def __getitem__(self, key: 'FakeSeries') -> 'FakeSeries':
        return FakeSeries(
            self.name,
            {i: v for i, v in self.data.items() if key.data.get(i, False)},
        )

    def __repr__(self) -> str:
        return f'<FakeSeries: {self.name} {self.data}>'



class FakeDataFrame:
    def __init__(self, d: Dict[str, List[Any]]):
        self.series_map = {
            k: FakeSeries(k, {i: v for i, v in enumerate(l)})
            for k, l in d.items()
        }
        self.length = len(list(d.values())[0])

    # handle []
    def __getitem__(self, key: str) -> FakeSeries:
        return self.series_map[key]

    # handle [] =
    def __setitem__(self, key: str, value: FakeSeries) -> None:
        if key not in self.series_map:
            self.series_map[key] = FakeSeries(key, {})
        for i, v in value.data.items():
            self[key].data[i] = v

    def __repr__(self):
        width = 5
        headers = ' | '.join(
            header.rjust(width)
            for header in self.series_map
        )
        divider = '-' * len(headers)
        rows = tuple(
            ' | '.join(
                str(self.series_map[k].data.get(i, 'NaN')).rjust(width)
                    for k in self.series_map
            )
            for i in range(self.length)
        )
        return '\n'.join((headers, divider) + rows) + '\n'
