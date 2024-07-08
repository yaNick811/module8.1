def add_everything_up(a, b):
    try:
        if type(a) != type(b):
            raise TypeError
        return a + b
    except TypeError:
        return f"{a}{b}"
    
# Примеры использования:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))