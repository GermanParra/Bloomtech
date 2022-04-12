import pytest
from helper_functions import random_phrase

def test_random_phrase_list_inputs():
    list1 = ['German']
    list2 = ['Parra']
    assert random_phrase(list1, list2) == 'German Parra'
    
def test_random_phrase_two_list_imputs():
    list1 = ['blue','red']
    list2 = ['square','circle']
    assert type(random_phrase(list1, list2)) == str

def test_random_phrase_int_list_imputs():
    list1 = [1, 2]
    list2 = [3, 4]
    assert type(random_phrase(list1, list2)) == str