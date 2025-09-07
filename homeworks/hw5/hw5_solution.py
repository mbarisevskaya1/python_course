def add_ing(s: str) -> str:
    s += 'ing'
    return s


def change_symbol(s: str) -> str:
    s1 = s.replace("#", '/')
    return s1


def change_order(s: str) -> str:
    s1 = s.split()
    s2 = s1[::-1]
    s3 = " ".join(s2)
    return s3


def clean_string(s: str) -> str:
    s1 = s.strip()
    return s1


def to_capitalize(s: str) -> str:
    s1 = s.capitalize()
    return s1


def to_list(s: str) -> list:
    s1 = s.split()
    return s1


def formatting(array: list, s1: str, s2: str) -> str:
    array1 = " ".join(array)
    s3 = "Привет, " + array1 + "! Добро пожаловать в " + s1 + " " + s2
    return s3


def to_string(array: list) -> str:
    s1 = " ".join(array)
    return s1


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array1 = array.copy()
    array1.insert(indx, item)
    return array1


def delete_from_list(array: list, indx: int) -> list:
    del array[indx]
    return array
