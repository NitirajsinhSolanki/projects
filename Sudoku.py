def intersection(list1, list2):
    intersec=[]
    for x in list1:
        for y in list2:
            if x == y:
                intersec.append(x)
    return intersec

def rowAvailibilty(numbers , aval):
    row_num=1
    for row in numbers:
        col_num=1
        avalible=[1,2,3,4,5,6,7,8,9]
        for digit in row:
            if digit !=0:
                avalible.remove(digit)       
        for digit in row:
            if digit == 0:
                aval[(row_num, col_num)] = avalible
            else:
                aval[(row_num, col_num)] = digit
            col_num +=1
        row_num += 1
    return aval

def colAvailibilty(numbers, aval):
    col_num=1
    for col_spot in range(1,10):
        row_num=1
        avalible=[1,2,3,4,5,6,7,8,9]
        for row_spot in range(1,10):
            if numbers[row_spot-1][col_spot-1] != 0:
                avalible.remove(numbers[row_spot-1][col_spot-1])
        for row_spot in range(1,10):
            if numbers[row_spot-1][col_spot-1] == 0 :
                avalibilty[(row_num, col_num)]= intersection(avalible,avalibilty[(row_num, col_num)])
            row_num += 1
        col_num += 1
    return aval

def propigate(numbers, aval):
    aval = rowAvailibilty(numbers, aval)
    aval = colAvailibilty(numbers, aval)
    for entry in aval:
        if isinstance(entry, list):
            if len(entry) == 0:
                #back track
                return null
            else:
                return aval

def _rowcheck(row, colum, numbers, aval):
       

def choose(numbers, aval):
    least_constraind=[]
    smallest=100
    for spots in aval.keys():
        if isinstance(aval[spots], list):
            if len(aval[spots]) < smallest:
                least_constraind.clear()                
                least_constraind.append(spots)
                smallest = len(aval[spots])
    if smallest == 1:
        for spots in least_constrained:
           for x,y in spots:
               numbers[x][y] = aval[spots][0]
    most_constraining=[]
    contrained=0
    for spots in least_constraind:
        
    return numbers

print('enter file name')
file=open('s01a.txt','r')
lines = file.readlines()
numbers=[]
past_states=[]

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

#solving star
avalibilty={}
avalibilty = rowAvailibilty(numbers,avalibilty)
print(avalibilty)

avalibilty = propigate(numbers,avalibilty)