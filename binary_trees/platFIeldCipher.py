import numpy as np


def t2n(t):
    return [ord(c) - ord("A") for c in t.upper()]


def n2t(n):
    return "".join([chr(num % 26 + ord("A")) for num in n])


def mod_inv(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 0:
            continue
        if (a * x) % m == 1:
            return x
    raise Exception(f"No modular inverse for {a} under mod {m}")


def m_inv_2x2_mod26(m):
    det = int(np.round(np.linalg.det(m)))
    det_inv = mod_inv(det % 26)
    adj = np.array([[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]])
    inv_m = (det_inv * adj) % 26
    return inv_m.astype(int)


def encrypt(p, k):
    p = p.upper().replace(" ", "")
    if len(p) % 2 != 0:
        p += "X"
    c = ""
    for i in range(0, len(p), 2):
        pair = t2n(p[i : i + 2])
        v = np.array(pair).reshape(2, 1)
        enc_v = np.dot(k, v) % 26
        c += n2t(enc_v.flatten())
    return c


def decrypt(c, k):
    inv_k = m_inv_2x2_mod26(k)
    p = ""
    for i in range(0, len(c), 2):
        pair = t2n(c[i : i + 2])
        v = np.array(pair).reshape(2, 1)
        dec_v = np.dot(inv_k, v) % 26
        p += n2t(dec_v.flatten())
    return p


if __name__ == "__main__":
    k = np.array([[3, 3], [2, 5]])
    p = "RudraRathodq"
    print(f"Plaintext: {p}")
    c = encrypt(p, k)
    print(f"Encrypted: {c}")
    d = decrypt(c, k)
    print(f"Decrypted: {d}")
