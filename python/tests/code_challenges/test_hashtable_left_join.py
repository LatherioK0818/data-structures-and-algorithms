import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


def test_left_join_returns_correct_structure():
    # Setup
    synonyms = {"diligent": "employed", "fond": "enamored", "guide": "usher"}
    antonyms = {"diligent": "idle", "fond": "averse", "guide": "follow"}
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"]
    ]

    # Exercise
    actual = left_join(synonyms, antonyms)

    # Verify
    assert actual == expected, "Should match the expected output structure and content"

def test_left_join_handles_missing_antonyms():
    # Setup
    synonyms = {"outfit": "garb", "wrath": "anger"}
    antonyms = {"wrath": "delight"}
    expected = [
        ["outfit", "garb", None],  # None for missing antonyms
        ["wrath", "anger", "delight"]
    ]

    # Exercise
    actual = left_join(synonyms, antonyms)

    # Verify
    assert actual == expected, "Should correctly handle missing antonyms with None"

def test_left_join_with_empty_dictionaries():
    # Setup
    synonyms = {}
    antonyms = {}
    expected = []

    # Exercise
    actual = left_join(synonyms, antonyms)

    # Verify
    assert actual == expected, "Should handle empty dictionaries gracefully"
