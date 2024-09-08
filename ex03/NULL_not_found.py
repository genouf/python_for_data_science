from math import isnan


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None", type(object))
    elif object == '':
        print("Empty :", type(object))
    elif object is False:
        print("Fake : False", type(object))
    elif isinstance(object, (int, float)) and isnan(object):
        print("Cheese : nan", type(object))
    elif object == 0:
        print("Zero : 0", type(object))
    else:
        print("Type not found")
        return 1
    return 0
