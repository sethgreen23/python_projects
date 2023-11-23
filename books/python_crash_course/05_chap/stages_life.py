"""
Person stage of life
"""
def stage_life(age):
    """ Determine Person stage of life"""
    if age < 2:
        print("is a baby")
    elif age < 4:
        print("is a toddler")
    elif age < 13:
        print("is a kid")
    elif age < 20:
        print("is a teenager")
    elif age < 65:
        print("is an adult")
    elif age >= 65:
        print("is an elder")

stage_life(37)
