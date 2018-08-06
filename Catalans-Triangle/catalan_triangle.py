def catalan_triangle(depth, current):
    print(current)
    if depth != 0:
        next = [1]
        for i in range(1,len(current)):
            next.append(current[i])
            next[i] += next[i-1]
        next.append(next[-1])
        catalan_triangle(depth-1, next)
 
catalan_triangle(6, [1])
