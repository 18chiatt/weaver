from collections import deque
from typing import Callable, Deque, List, Mapping, Set
import pickle
import os
import sys


class Node:
    def __init__(self, word) -> None:
        self.word = word
        self.children = []


def getWords() -> List[str]:
    if not os.path.isfile("words.txt"):
        print("Please please please please add a 'words.txt' file to your current path :)")
        return None
    with open("words.txt", "r", encoding="utf-8") as file:
        words = file.readlines()
        words = filter(lambda w: not w.startswith("#!comment"), words)
        words = list(set(words))
        words = map(lambda w: w.strip(), words)
        words = filter(lambda w: len(w) == 4, words)
        words = list(map(lambda x: x.lower(), words))
        return words


def saveGraph(graph):
    print("Saving Graph")
    with open("wordGraph.pickle", "wb") as handle:
        pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)


def getGraph():
    if not os.path.isfile("wordGraph.pickle"):
        return None
    with open("wordGraph.pickle", "rb") as handle:
        b = pickle.load(handle)
    return b


def isPair(w1: str, w2: str) -> bool:
    distance = False
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            if distance:
                return False
            distance = True
    return True


def makeGraph(words: List[str]) -> Mapping[str, Node]:
    nodes = {}
    for word in words:
        nodes[word] = Node(word)
    for i1, w1 in enumerate(words):
        for i2, w2 in enumerate(words):
            if i1 != i2 and isPair(w1, w2):
                nodes[w1].children.append(w2)
                nodes[w2].children.append(w1)
    return nodes




def traceSolution(word: str, mapping: Mapping[str, str]) -> List[str]:
    path = []
    while word:
        path.append(word)
        word = mapping[word]
    return path


def findPath(graph: Mapping[str, Node], startWord: str, endWord: str):
    startQueue = deque([graph[startWord]])
    endQueue = deque([graph[endWord]])

    startBackPointers: Mapping[str, str] = {startWord: ""}
    endBackPointers: Mapping[str, str] = {endWord: ""}

    def doWork(
        fromQueue: Deque[Node],
        targetMap: Mapping[str, str],
        sourceMap: Mapping[str, str],
        solved: Callable[[List[str]], bool],
    ):
        def toReturn():
            if not fromQueue:
                return False
            item = fromQueue.popleft()
            for sibling in item.children:
                if sibling in sourceMap:
                    # Ignore!
                    continue
                if sibling in targetMap:
                    # Found SOlution!
                    solution = traceSolution(item.word, sourceMap)[
                        ::-1
                    ] + traceSolution(sibling, targetMap)
                    return solved(solution)
                sourceMap[sibling] = item.word
                fromQueue.append(graph[sibling])
            return False

        return toReturn

    def printSolution(sln: List[str]):
        print("Solution: ", sln)
        return True

    startExplore = doWork(startQueue, endBackPointers, startBackPointers, printSolution)
    endExplore = doWork(
        endQueue, startBackPointers, endBackPointers, lambda x: printSolution(x[::-1])
    )

    while startQueue or endQueue:
        if startExplore():
            break
        if endExplore():
            break

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print("Usage: python", sys.argv[0] + " sourceWord destinationWord")

    words = getWords()
    if not words:
        exit(1)

    graph = getGraph()
    if graph is None:
        graph = makeGraph(words)
        saveGraph(graph)

    findPath(graph, sys.argv[1], sys.argv[2])
