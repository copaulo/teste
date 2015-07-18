teste = True
dados = []
while True:
    if not teste:
        try:
            entrada = input()
            dados.append(entrada)
        except: break
    else:
        entrada  = input()
        if not entrada: break
        dados.append(entrada)

def last_to_die(n,k):
    n = list(range(1,n+1))
    pos = 0
    while len(n) > 1:
        pos+=k
        pos = (pos-1)%len(n)
        n.remove(n[pos])
    return n[0]

n = int(dados[0])
for i in range(1,n+1):
    n,k = [int(l) for l in dados[i].split(' ')]
    print('Case {}: {}'.format(i,last_to_die(n,k)))
