# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p): return p(lambda x, y: x)

def cdr(p): return p(lambda x, y: y)

def test_main():
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4 

if __name__ == "__main__":
    test_main()

# kotlin version
# fun car(p: ((Int, Int) -> Int) -> Int): Int {
#     return p({ a, _ -> a })
# }

# fun cdr(p: ((Int, Int) -> Int) -> Int): Int {
# 	return p({ _, b -> b})
# }

# fun cons(a: Int, b: Int): (f: (Int, Int) -> Int) -> Int {
#     return { f -> f(a, b) }
# }

# fun main() {
#     assert(car(cons(3, 4)) == 3)
#     assert(cdr(cons(3, 4)) == 4)
# }