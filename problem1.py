                                   
#String palindrone or not?
'''
st=list(input().strip())
l=''.join(st)

for i in range(len(st)//2):
    temp=st[len(st)-i-1]
    st[len(st)-i-1]=st[i]
    st[i]=temp
r=''.join(st)
if(r==l):
    print("True")
else:
    print("False")
'''    
#------------------------------------------------------------------
'''
try:
    
    l=[1,2,3,4]
    l.remove(5)
    print(l)
except ValueError as v:
    print("error")
'''
# Removing element from array
'''
st=list(input().strip())
ch=input().strip()

for i in st:
    if(i==ch):
        st.remove(i)
print(st)
'''
# Finding and deleting first occurence of  an element in array
''''
st=list(input().strip())
ch=input().strip()

for i in st:
    if(i==ch):
        st.remove(i)
print(st)
'''
'''
try:
    ch='p'
    l=['l','k','p','p']
    l.remove(ch)
    print(l)
except ValueError:
    pass
'''
'''
st=list(input())
ch=input()

while(ch in st):
    st.remove(ch)
print(st)
'''
#-------------------------------------------
'''
def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        print(''.join(string))
    for i in range(step, len(string)):
        string_copy = [c for c in string]
         # swap the current index with the step
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
         # recurse on the portion of the stringthat has not been swapped yet
        permutations(string_copy, step + 1)
print(permutations ('one'))
'''
'''
text = input()
l1 = list(text)

for i in range(len(l1)):
    if(l1.count(l1[i]) > 1):
        for j in range(i+1, len(l1)):
            if(l1[i] == l1[j]):
                l1[j]='0'

l = ''.join(l1)

print(''.join(l.split('0')))
'''
# How to find the maximum occurring character in given String
'''
l=list(input())
print(l)
l1=[]

for i in range(len(l)):
    n=l.count(l[i])
    l1.append(n)

m=l1.index(max(l1))
print(l[m])
'''

#How to remove all duplicates from a given string
'''
l=list(input())
for i in range(len(l)):
    if(l.count(l[i])>1):
        for j in range(i+1,len(l)):
            if(l[j]==l[i]):
                l[j]='0'
l1=''.join(l)
print(''.join(l1.split('0')))
'''
#How to print the duplicate characters from the given String
'''
l=list(input())
l1=[]
for i in range(len(l)):
    if(l.count(l[i])>1 and l[i] not in l1):
        
        l1.append(l[i])
print(l1)
'''


#---------------------------------------- -----------------------------
'''
def linear(array,key):
    for i in range(len(array)):
        if(array[i]==key):
            return i
    return -1
data=[2,5,9,7,0,3]
key=3
re=linear(data,key)
if(re==-1):
    print("not")
else:
    print(re)
'''



