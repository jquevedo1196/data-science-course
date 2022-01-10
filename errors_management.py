def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
    except TypeError:
        print("Solo se pueden ingresar strings")
        return False

def palindrome_with_asserts(string):
    assert type(string) == str, "Solo se acepta texto"
    assert len(string) > 0, "No se pueden ingresar cadenas vacías"
    return string == string[::-1]
    
if __name__ == '__main__':
    #print(palindrome(1))
    print(palindrome_with_asserts(11))