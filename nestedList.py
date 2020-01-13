# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    lista = []
    notas = []
    result = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append((name,score))
    
    for nota in lista:
        notas.append(nota[1])
    
    notas.sort()
    
    min_nota = notas[0]
    i = 0
    
    del notas[0]
    
    while notas[i] == min_nota:
        i += 1
    
    seg_min_nota = notas[i]
    
    for aluno in lista:
        if aluno[1] == seg_min_nota:
            result.append(aluno)
    
    result.sort()
    
    for i in result:
        print(i[0])
