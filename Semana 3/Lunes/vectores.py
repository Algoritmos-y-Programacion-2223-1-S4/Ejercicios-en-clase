vec1 = [1,2,3]
vec2 = [-1,0,2]
acum_total= 0

for index in range(len(vec1)):
    acum_total+= (vec1[index]*vec2[index])

print("Result:",acum_total)