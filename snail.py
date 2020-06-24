size = int(input("크기를 입력해주세요 : "))
matrix = [[0]*size for i in range(size)]
space = 0
w = 0 #width
h = -1 #height
d = 1
def square(size, w, h, space, d): #(갯수,)
    if size == 0: #사각형 초기화
        return 0
    for n in range(1, size + 1):
        h = h + d
        space += 1
        matrix[w][h] = space
    size = size -1
    for n in range(1, size + 1):
        w = w + d
        space += 1
        matrix[w][h] = space
    d = d * -1
    return square(size, w, h, space, d)

square(size, w, h, space, d)
for w in range(size):
    print(matrix[w])
