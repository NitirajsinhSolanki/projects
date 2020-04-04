
def intersection(list1, list2):
    intersec=[]
    for x in list1:
        for y in list2:
            if x == y:
                intersec.append(x)
    return intersec

def rowAvailibilty(numbers , avalibilty):
    row_num=1
    for row in numbers:
        col_num=1
        avalible=[1,2,3,4,5,6,7,8,9]
        for digit in row:
            if digit !=0:
                if digit in avalible:
                    avalible.remove(digit)       
        for digit in row:
            if digit == 0:
                avalibilty[(row_num, col_num)] = avalible
            else:
                avalibilty[(row_num, col_num)] = digit
            col_num +=1
        row_num += 1
    return avalibilty

def colAvailibilty(numbers, avalibilty):
    col_num=1
    for col_spot in range(1,10):
        row_num=1
        avalible=[1,2,3,4,5,6,7,8,9]
        for row_spot in range(1,10):
            if numbers[row_spot-1][col_spot-1] != 0:
                if numbers[row_spot-1][col_spot-1] in avalible:
                    avalible.remove(numbers[row_spot-1][col_spot-1])
        for row_spot in range(1,10):
            if numbers[row_spot-1][col_spot-1] == 0 :
                avalibilty[(row_num, col_num)]= intersection(avalible,avalibilty[(row_num, col_num)])
            row_num += 1
        col_num += 1
    return avalibilty

def cellAvailibilty(numbers, avalibilty):
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(0,3):
        for col in range(0,3):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
        if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]

    for row in range(0,3):
        for col in range(3,6):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
        if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(0,3):
        for col in range(6,9):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(3,6):
        for col in range(0,3):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(3,6):
        for col in range(3,6):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(3,6):
        for col in range(6,9):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(6,9):
        for col in range(0,3):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(6,9):
        for col in range(3,6):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    avalible=[1,2,3,4,5,6,7,8,9]
    keyset=[]
    for row in range(6,9):
        for col in range(6,9):
            if numbers[row][col] != 0:
                avalible.remove(numbers[row][col])
                keyset.append((row+1,col+1))
    for keys in keyset:
         if isinstance(avalibilty[keys],list):
            avalibilty[keys]=intersection(avalibilty[keys],avalible)
    return avalibilty

def finishCheck(numbers):
    for rows in numbers:
        for number in rows:
            if number == 0:
                return True    
    return False

def removeVisited(avalibilty, visited):
    for spots in visited.keys():
        if isinstance(avalibilty[spots],list):
            intersec = intersection(avalibilty[spots], visited[spots])
            for temp in intersec:
                avalibilty[spots].remove(temp)
    return avalibilty

def propigate(numbers, avalibilty, visited):
    avalibilty = rowAvailibilty(numbers, avalibilty)
    avalibilty = colAvailibilty(numbers, avalibilty)
    avalibilty = cellAvailibilty(numbers, avalibilty)
    avalibilty = removeVisited(avalibilty, visited)
    for entry in avalibilty:
        if isinstance(entry, list):
            if len(entry) == 0:
                #backtrack(numbers, past_states)
               return 0;
    return avalibilty

def _rowcheck(row, numbers):
       counter = 0
       for col in range (0,9):
           if numbers[row-1][col] == 0:
               counter += 1
       return counter

def _colcheck(col, numbers):
    counter = 0
    for row in range(0,9):
        if numbers[row][col-1] == 0:
            counter +=1
    return counter

def choose(numbers, avalibilty, visited):
    least_constrained=[]
    smallest=100
    for spots in avalibilty.keys():
        if isinstance(avalibilty[spots], list):
            if len(avalibilty[spots]) < smallest:
                least_constrained.clear()                
                least_constrained.append(spots)
                smallest = len(avalibilty[spots])
            if len(avalibilty[spots]) == smallest:
                least_constrained.append(spots)
    if smallest == 1:
        for spots in least_constrained:
            numbers[spots[0]][spots[1]] = avalibilty[spots][0]
    most_constraining=[]
    contrained=0
    for spots in least_constrained:
        current_contrained = _rowcheck(spots[0], numbers)+ _colcheck(spots[1], numbers)
        if current_contrained > contrained:
            most_constraining.clear
            most_constraining.append(spots)
        if current_contrained == contrained:
            most_constraining.append(spots)

    picked_spot = most_constraining[0]
    value = avalibilty[picked_spot][0]
    if picked_spot in visited:
        visited[picked_spot].append(value)
    else:
        visited[picked_spot]=[value]
    
    numbers[picked_spot[0]][picked_spot[1]]=value
    return numbers

def backtrack(numbers, visited, tracked):
    
    return numbers

print('enter file name')
file=open('s01a.txt','r')
lines = file.readlines()
numbers=[]
visited={}
tracked={}

#initial run
for x in lines:
    number_row=[]
    for digit in x:
        if digit != ' ' and digit !='\n':
            number_row.append(int(digit))
    if len(number_row) > 0:
        numbers.append(number_row)

#check
print(numbers)
print('needed change for commit')
#solving star
avalibilty={}
while finishCheck(numbers):
    avalibilty=propigate(numbers, avalibilty, visited)
    numbers= choose(numbers, avalibilty, visited)