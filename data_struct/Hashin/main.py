"""
# crete hash table implementation
# python already implemented hash table as 
# Pythons Dictionary data struck
"""
from ClassData import Some
from SeperateChaining import Table


def my():
    s1 = Some("data 1")
    s2 = Some("data 2")
    s3 = Some("data 3")

    print(f"{s1} , {s2} , {s3}")

    t = Table(4)

    t.show_all()


def saperate_chain_aproch():
    t = Table(5)

    s1 = Some("data 1")
    s2 = Some("data 2")
    s3 = Some("data 3")
    s4 = Some("data 4")
    s5 = Some("data 5")
    s6 = Some("data 6")

    t.push(s1).push(s2).push(s3).push(s4).push(s5).push(s6)

    t.show_all()

    print("=================================\n")
    print(f"s6 inside {t.is_inside(s6)}")
    print(f"pop ->  : {s6}")
    t.pop(s6)
    t.show_all()


if __name__ == "__main__":
    # saperate_chain_aproch()
    pass
