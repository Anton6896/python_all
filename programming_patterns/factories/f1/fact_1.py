from math import cos, sin


class Point_1:
    """ 
    factory initialization for couple types of object that have an same structure 
    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point_1(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point_1(rho*sin(theta), rho * cos(theta))

    def __str__(self):
        return f"({str(round(self.x, 2))}, {str(round(self.y, 2))})"


if __name__ == "__main__":
    p1 = Point_1(12, 5)
    p2 = Point_1.new_polar_point(2, 5)

    print(
        f"point : {p1} \npolar point {p2}"
    )
