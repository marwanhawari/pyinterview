<p align="center">
  <img width=70% height=auto src="https://github.com/marwanhawari/pyinterview/raw/main/docs/pyinterview_logo.png" alt="pyinterview logo"/>
</p>

[![PyPI version](https://badge.fury.io/py/pyinterview.svg)](https://badge.fury.io/py/pyinterview)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyinterview)](https://pypi.org/project/pyinterview/)
[![Build Status](https://github.com/marwanhawari/pyinterview/actions/workflows/build.yml/badge.svg)](https://github.com/marwanhawari/pyinterview/actions)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/marwanhawari/pyinterview/blob/main/CODE_OF_CONDUCT.md)
[![Documentation Status](https://img.shields.io/github/workflow/status/marwanhawari/pyinterview/docs?label=docs)](https://www.pyinterview.org/)
[![GitHub](https://img.shields.io/github/license/marwanhawari/pyinterview?color=blue)](https://github.com/marwanhawari/pyinterview/blob/main/LICENSE)

# Description
This library contains useful data structures and algorithms that are commonly used in coding interviews. The goal of this project is to provide modules that can actually be used to solve interviewing problems. This project is NOT a code dump of solutions to interviewing problems. The classes and functions were designed to be compatible with LeetCode.

# Installation
The `pyinterview` package can be installed directly using `pip`.
```
pip install pyinterview
```

# Usage
Users can import common data structures and algorithms from several different modules. For example:<br>

* To manually construct a binary tree, import the `TreeNode` class from the `trees` module:
```python
from pyinterview.trees import TreeNode

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
```

* To construct a undirected graph adjacency list, import the `undirected_adj_list` function from the `graphs` module:
```python
from pyinterview.graphs import undirected_adj_list

edges = [('A', 'B'), ('A', 'C'), ('C', 'D')]
adj_list = undirected_adj_list(edges)
```


# Documentation
The documentation is a work in progress, but contributions are welcome!

[pyinterview documentation](https://pyinterview.org)
