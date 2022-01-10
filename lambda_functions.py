from functools import reduce

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    palindrome = lambda word: word == word[::-1]
    print(palindrome("hola"))

    list_el = [1, 4, 5, 6, 9, 13, 19, 21]
    print(list_el)

    list_el = list(filter(lambda element: element % 2 != 0, list_el))
    print(list_el)

    list_el = [1, 2, 3, 4, 5]
    list_el = list(map(lambda element: element**2, list_el))
    print(list_el)

    list_el = [2, 2, 2, 2, 2]
    list_el = reduce(lambda a, b: a * b, list_el)
    print(list_el)

def project():
    filtered_list = list(map(lambda element: element['name'],filter(lambda element: (element['organization'] == "Platzi" or element['language'] == "python"), DATA )))
    print(filtered_list)
    print(len(filtered_list))


if __name__ == '__main__':
    #run()
    project()
