# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    i = 0
    media = 0
    
    for notas in student_marks[query_name]:
        media += notas
        i += 1
    
    media = media / i
    
    print(f'{media:.2f}')
