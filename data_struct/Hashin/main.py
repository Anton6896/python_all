# crete hash table implementation 
# python already implemented hash table as Pythons Dictionary data struck 
from ClassData import Some
from TableMy import Table


def my():
    s1 = Some("data 1")
    s2 = Some("data 2")
    s3 = Some("data 3")

    print(f"{s1} , {s2} , {s3}")

    t = Table(4)

    t.show_all()


def check_t():
    t = Table(5)
    s1 = Some("data 1")
    s6 = Some("data 6")

    t.add_to(s1)
    t.add_to(Some("data 2"))
    t.add_to(Some("data 3"))
    t.add_to(Some("data 4"))
    t.add_to(Some("data 5"))
    t.add_to(s6)
    s7 = Some("data 7")
    t.add_to(s7)

    t.show_all()

    print(f"\n is inside {t.is_inside(s6)}")

    print("=================================")
    print(s7)
    t.remove_at(s7)
    t.show_all()


if __name__ == "__main__":
    check_t()
