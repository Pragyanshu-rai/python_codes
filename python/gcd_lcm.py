def gcd(a, b):
  if a == 0:
    return b;
  if b == 0:
    return a;
  if a>b:
    return gcd(a%b, b);
  return gcd(a, b%a);

def lcm(a, b):
  return (a*b)//gcd(a, b);

print(gcd(10, 32));

print(lcm(12, 5));