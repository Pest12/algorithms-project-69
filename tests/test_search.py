
from search_engine.search_engine import search

DOC1 = "I can't shoot straight unless I've had a pint!"
DOC2 = "Don't shoot shoot shoot that thing at me."
DOC3 = "I'm your shooter."
DOCS = [
    {'id': 'doc1', 'text': DOC1},
    {'id': 'doc2', 'text': DOC2},
    {'id': 'doc3', 'text': DOC3},
]


def test_search():
    assert search(DOCS, 'shoot') == ['doc1', 'doc2']


def empty_test_search():
    assert search([], 'shoot') == []