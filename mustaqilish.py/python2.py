a=10; b=3.1456; c=True; d='Fondation'
print("a={} b={} c={} d={}".format(a,b,c,d))
print("a={1} b={0} c={3} d={2}".format(a,b,c,d))
print("a={1} b={1} c={1} d={1}".format(a,b,c,d))
print(f"a={a} b={b} c={c} d={d}")
print("a={:05d} b={:.2f} c={} d={}".format(a,b,c,d))