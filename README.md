# Weaver

Weaver is a wordgame in which players seek to find the shortest paths between two 4 letter words. A Path consists of a sequence of one or more words which differs from its neighbors by exactly one letter. The goal of the game is to find the shortest path possible between the start and end words.

## Usage

To run the program, provide a start and end word. Use the included words.txt, or create your own.

```bash
python3 dfs.py startWord endWord
```

Example Output

```text
Solution:  ['bone', 'bane', 'base', 'bast', 'cast']
```
