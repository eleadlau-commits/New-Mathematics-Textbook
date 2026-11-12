# Chapter 30 check: the two homes of a wave (numerical).
import numpy as np
K = 1 << 15; t = (np.arange(K) + 0.5) / K
w = lambda s: np.exp(2j*np.pi*s)
N = 2000
def coefs(f): 
    F = np.fft.fft(f) / K  # midpoint grid: c_n = exp(-i pi n/K) * F[n]
    return {n: F[n % K]*np.exp(-1j*np.pi*n/K) for n in range(-N, N + 1)}
maps = {"exp(cos)": np.exp(np.cos(2*np.pi*t)), "|sin|": np.abs(np.sin(2*np.pi*t)),
        "square": np.where(t < 0.5, 1.0, -1.0), "sawtooth": t - 0.5}
for name, f in maps.items():
    c = coefs(f); E = sum(abs(v)**2 for v in c.values()); nrm = np.mean(np.abs(f)**2)
    gaps = []
    for M in (10, 100, 1000):
        S = sum(c[n]*w(n*t) for n in range(-M, M + 1)); gaps.append(np.sqrt(np.mean(np.abs(f - S)**2)))
    print("T1 %-9s energy %.6f vs ||f||^2 %.6f ; mean-square gap of S_N at N=10,100,1000:" % (name, E, nrm), ["%.4f" % g for g in gaps])
for name, cl in (("1/(1+n^2)", lambda n: 1/(1 + n*n)), ("1/n", lambda n: 0 if n == 0 else 1/n)):
    f = sum(cl(n)*w(n*t) for n in range(-N, N + 1)); c = coefs(f)
    print("T2 list %s reproduced:" % name, all(abs(c[n] - cl(n)) < 1e-9 for n in range(-20, 21)))
c = coefs(maps["sawtooth"])
print("T3 sawtooth coefficients i/(2 pi n):", all(abs(c[n] - 1j/(2*np.pi*n)) < 1e-6 for n in (1, 2, 3, 10)), " ||f||^2 = 1/12:", abs(np.mean((t - 0.5)**2) - 1/12) < 1e-9, " sum 1/n^2 -> pi^2/6:", abs(sum(1/n**2 for n in range(1, 10**6)) - np.pi**2/6) < 1e-5)
f, g = maps["exp(cos)"], maps["sawtooth"] * (1 + 1j)
ip = np.mean(f*np.conj(g)); pol = sum((1j**k)*np.mean(np.abs(f + (1j**k)*g)**2) for k in range(4))/4
print("Polarisation:", abs(ip - pol) < 1e-12)
print("E1 square wave: sum over odd n of 1/n^2 = pi^2/8:", abs(sum(1/n**2 for n in range(1, 10**6, 2)) - np.pi**2/8) < 1e-5)
