"""
in pycharm setting need to change the unittest to the pytest as main option for this project
"""


def vowels(text: str):
    """
    count amount of vowels in given text
    :param text: some text
    :return: integer
    """
    amount = 0
    vowels_list = ['a', 'u', 'i', 'e', 'o', ]
    for ch in text.lower():
        if ch in vowels_list:
            amount += 1
    return amount


def test_vowel_test_1():
    assert vowels('carlos') == 2


def test_vowel_test_2():
    assert vowels('Ant') == 1


if __name__ == '__main__':
    test_vowel_test_2()
    test_vowel_test_1()
