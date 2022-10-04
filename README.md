# Weaver

Weaver is a wordgame in which players seek to find the shortest paths between two 4 letter words. A Path consists of a sequence of one or more words which differs from its neighbors by exactly one letter. The goal of the game is to find the shortest path possible between the start and end words.

## Usage

To run the program, provide a start and end word. Use the included words.txt, or create your own. The first run is a bit slower because it needs to generate the word graph, but subsequent runs will be very fast. If you update the dictionary file (word.txt) you will need to delete the wordGraph.pickle file that gets generated to clear the cache.

```bash
python3 dfs.py startWord endWord
```

Example Output

```text
> python3 dfs.py bone cast
Solution:  ['bone', 'bane', 'base', 'bast', 'cast']
```
