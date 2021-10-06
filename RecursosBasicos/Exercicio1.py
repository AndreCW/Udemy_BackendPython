import sys

notas = list(map(int,sys.argv[1:]))
novas = [(lambda ng: ((int(ng/5)+1)*5) if ng > 60 and ((int(ng/5)+1)*5) - ng < 3 else ng)(ng) for ng in notas]
print(novas)