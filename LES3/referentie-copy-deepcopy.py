import copy


def referentie_uitleg():
    print("\n_____ referentie - (x=y) _____")
    old_list = [[1,2,3],
                [4,5,6],
                [7,8,"String"]]
    print("old: ", old_list)
    new_list = old_list
    print("new: ", new_list)

    print("oldlist[2][2]: ",old_list[2][2])

    old_list[2][2] = True
    print("OLD: ", old_list)
    print("NEW: ", new_list)
    print("id:",id(old_list))
    print("id:",id(new_list))

def shallow_copy():
    import copy
    print("\n_____ shallow - copy(x=copy(y)) _____")
    old_list = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, "String"],
                "true"]

    new_list = copy.copy(old_list)
    new_list[3] = "4de Element"
    print("OLD: ", old_list)
    print("NEW: ", new_list)

    print("id:",id(old_list))
    print("id:",id(new_list))

def deep_copy():
    import copy
    print("\n_____ deep copy - (x=deepcopy(y)) _____")
    old_list = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, "String"],
                "true"]

    new_list = copy.deepcopy(old_list)
    new_list[0][0] = "eerste"
    print("OLD: ", old_list)
    print("NEW: ", new_list)

    print("id:",id(old_list))
    print("id:",id(new_list))
if __name__ == '__main__':
    referentie_uitleg()
    shallow_copy()
    deep_copy()