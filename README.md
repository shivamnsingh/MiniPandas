# MiniPandas

A small pandas-like DataFrame/Series library built from scratch in pure Python — no dependencies — to understand how libraries like pandas actually work under the hood, and to practice object-oriented design.

## Why I built this

I wanted to go beyond just *using* pandas and actually understand what's happening when you call `df.groupby("col").mean()` or `df[df["col"] > 5]`. Building a mini version forced me to think through real OOP design problems: how do you implement Python's data model (`__getitem__`, `__eq__`, `__gt__`) so your objects behave naturally, and how do you design an intermediate object (`GroupedDataframe`) to support method chaining like `groupby(...).mean()`.

## Features

- `Series` and `Dataframe` classes with core dunder methods (`__repr__`, `__len__`, `__eq__`, `__gt__`, `__getitem__`, `__str__`)
- Column selection: `df["Age"]`
- Multi-column selection: `df[["Name", "Age"]]`
- Boolean filtering: `df[df["Age"] > 20]`
- `sort_values()`, `drop()`, `head()`, `shape`, `info()`
- `groupby()` returning a `GroupedDataframe`, with `.mean()`, `.sum()`, `.count()` aggregations

## Example usage

```python
from minipandas import Dataframe

data = [
    ["Shivam", 20, 60],
    ["Rahul", 21, 55],
    ["Aman", None, 30],
    ["Raj", 22, 40],
    ["Vivek", 20, 22],
    ["Shivam", 21, 45],
]
columns = ["Name", "Age", "Weight"]

df = Dataframe(data, columns)

print(df["Age"])                        # column selection
print(df[df["Age"] > 20])               # boolean filtering
print(df.groupby("Age").mean())         # groupby + aggregation
```

See `demo.py` for a full walkthrough of every feature.

## Design notes: how `groupby()` works

`groupby("Age")` doesn't compute anything immediately. It:
1. Finds the position of the `"Age"` column
2. Walks through every row, bucketing full rows into a dict keyed by their `Age` value
3. Wraps that dict in a `GroupedDataframe`, which also remembers *which* column was grouped on

`GroupedDataframe.mean()` / `.sum()` / `.count()` then loop through each group, skip the groupby column itself (averaging a group's own label against itself is meaningless), skip non-numeric columns where relevant (you can't average a name), and build one output row per group.

This mirrors, at a small scale, how pandas separates "group the data" from "aggregate the data" into two distinct steps/objects.

## Running tests

```bash
python tests/test_minipandas.py
```

## What's not implemented

This isn't meant to be feature-complete with pandas — no indexing beyond position, no `NaN`-specific handling beyond `None`, no `isnull()`/`fillna()`/`describe()` yet. The goal was depth on a few core mechanisms (indexing, filtering, grouping) rather than breadth across all of pandas' API.

## Project structure

```
MiniPandas/
├── README.md
├── minipandas.py       # Series, Dataframe, GroupedDataframe
├── demo.py             # usage examples
├── requirements.txt
└── tests/
    └── test_minipandas.py
```
