def transformation(line_a, line_b, line_c):
   dictionary = {}

   for line in (line_a, line_b, line_c):
       for id, count in line:
           if id not in dictionary:
               dictionary[id] = [0, 0, 0]
          
           index = (line_a, line_b, line_c).index(line)
           dictionary[id][index] = count

   return dictionary

line_a = ((1, 3), (3, 4), (10, 2))
line_b = ((1, 2), (2, 4), (5, 2))
line_c = ((1, 5), (3, 2), (7, 3))

result = transformation(line_a, line_b, line_c)
print(result)

