import math
def gcd_mod_k(a, b, k):
    result_gcd = math.gcd(a, b)
    return result_gcd % k
a, b, k = 48, 18, 5
print(f"GCD({a}, {b}) % {k} =", gcd_mod_k(a, b, k))
