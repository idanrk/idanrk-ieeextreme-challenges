# BASE 62 conversion credit: https://stackoverflow.com/questions/1119722/base-62-conversion
# Challenge Link: https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/shortening-in-the-real-world/problem
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode_62(num, alphabet=BASE62):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


# http://www.ieee.com
# http://www.ieee.org/xtreme
base_url = input()
n = int(input())
for _ in range(n):
    b_url = bytes(base_url, 'utf-8')
    target = input()
    t_url = bytes(target, 'utf-8')
    # done with first stage
    while (len(b_url) != len(t_url)):
        if len(b_url) < len(t_url):
            b_url = b_url + b_url[:len(t_url) - len(b_url)]  # adding bits to base
        elif len(b_url) > len(t_url):
            b_url = b_url[:len(t_url)]  # shortening the base to target length
    # finished stage 2
    """print(f"The base url: {b_url} , its length = {len(b_url)}", end='\n')
    print(f"The target url: {t_url} , its length = {len(t_url)}", end='\n')"""
    result = b''.join([bytes([a ^ b]) for (a, b) in zip(b_url, t_url)])
    # take the last 8 bytes and convert to unsigned int
    print(base_url + '/' + encode_62(int.from_bytes(result[-8:], "big", signed=False)))
