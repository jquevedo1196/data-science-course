def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "John", "last_name": "Doe"}

    super_list = [
        {"first_name": "John1", "last_name": "Doe1"},
        {"first_name": "John2", "last_name": "Doe2"},
        {"first_name": "John3", "last_name": "Doe3"},
        {"first_name": "John4", "last_name": "Doe4"},
        {"first_name": "John5", "last_name": "Doe5"}
    ]

    super_dict = {
       "natural_nums": [1,2,3,4,5],
       "integer_nums": [-2, -1, 0, 1, 2,],
       "floating_nums": [1.1, 2.2, 3.3, 4.5, 5.5]
    }

    for k, v in super_dict.items():
        print(k, "-", v)
    
    for value in super_list:
        print(value.get("first_name"), "-", value.get("last_name"))

    for key, value in my_dict.items():
        print(key, "-", value)
    
    for value in my_list:
        print(value)

    my_natural_list = [i*i for i in range(1, 101) if i % 3 != 0]
    print(my_natural_list)
    print(len(my_natural_list))

    
    my_mcm_list = [i for i in range(1, 9999) if i % 9 == 0 and i % 6 == 0 and i % 4 == 0]
    print(my_mcm_list)
    print(len(my_mcm_list))
    
    my_cube_dict = {i:i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_cube_dict)
    print(len(my_cube_dict))
    



if __name__ == '__main__':
    run()
