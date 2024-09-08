def all_thing_is_obj(object: any) -> int:
    typeObject = type(object)

    if typeObject == list:
        print("List : ", typeObject)
    elif typeObject == tuple:
        print("Tuple : ", typeObject)
    elif typeObject == set:
        print("Set : ", typeObject)
    elif typeObject == dict:
        print("Dict : ", typeObject)
    elif typeObject == str:
        if object == "Brian":
            print("Brian is in the kitchen : ", typeObject)
        elif object == "Toto":
            print("Toto is in the kitchen : ", typeObject)
    else:
        print("Type not found")

    return 42