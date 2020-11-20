def isprime(num):
    if num <=1:
        return 0
    if num <=3:
        return 1
    x=2
    while x<=num//2:
        if num%x==0:
            return 0
        x+=1
    return 1
def p_range(ln,un):
    prime_num=list()
    for i in range(ln,un+1):
        if isprime(i) == 1:
            prime_num.append(i)
    return prime_num
def p_nums(ln,un):
    num_sum=0
    count=0
    prime_num=p_range(ln,un)
    for i in prime_num:
        num_sum+=i
        if num_sum == 2:
            continue
        if isprime(num_sum) == 1:
            count+=1
            #print(num_sum)
        if num_sum > un:
            break
    return count
print(p_nums(0,36000))
