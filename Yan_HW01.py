def classify_triangle(a: int, b: int, c: int) -> str:
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "It is an equilateral triangle, but not a right triangle."
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a ** 2:
                return "It is an isosceles triangle, and a right triangle."
            else:
                return "It is an isosceles triangle, but not a right triangle."
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a ** 2:
            return "It is a scalene triangle, and a right triangle."
        else:
            return "It is a scalene triangle, but not a right triangle."
    else:
        return "Unable to form a triangle."

if __name__ == "__main__":
    """main function"""
    a, b, c = map(int, input("Please input the lengths of three sides of a triangle(split by ','): ").split(","))
    print(classify_triangle(a, b, c))