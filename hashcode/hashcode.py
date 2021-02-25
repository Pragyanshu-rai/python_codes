fname = input()

if len(fname) < 1:
    fname = 'a.txt'

fin = open(fname, 'rt')

inp = fin.readline().strip().split(" ")

intersection = int(inp[1])

streets = int(inp[2])

cars = int(inp[3])

index=0

street_to_inter = dict()

inter_street = dict()

inter_mul_stre = dict()

while index < streets:
    
    line = fin.readline().strip().split(" ")
    
    key = line[2] # street name
    
    value = int(line[1]) # end point of street or end intersection
    
    street_to_inter[key] = value

    inter_street[value] = inter_street.get(value, 0) + 1
    
    inter_mul_stre[value] = inter_mul_stre.get(value , "") + key + ' ' + '1' + '\n'
    
    index += 1

index=0

route = list()    

while index < cars:
    
    line = fin.readline().strip().split(" ")
    
    line = line[1:-1]
    
    for street in line:
        if street not in route:
            route.append(street)
    
    index += 1

intersections=list()

for street in route:
    
    if street_to_inter[street] not in intersections:
        
        intersections.append(street_to_inter[street])
        
for index in range(len(intersections)):
    
    intersections[index] = str(intersections[index])+'\n'+str(inter_street[intersections[index]])+'\n'+inter_mul_stre[intersections[index]]
    

intersections.insert(0, str(len(intersections))+'\n')

#print(street_to_inter)

#print(route)

#print(intersections)

fout = open(fname[0:1]+'out.txt', 'w')

for string in intersections:
    fout.write(string)

#print(inter_street)

#print(inter_mul_stre)

fin.close()

fout.close()


