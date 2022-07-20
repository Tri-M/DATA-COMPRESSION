f=open("huffman.txt","r")
s=f.readline()
s=s.replace(" ","")
s=s.lower()
chars=list(set(s))    #unique chars 
print("The string is : ",s)
print("Characters : ",chars)
length=len(chars)
print(length)
freq=[0]*length
for i in s:
    count=s.count(i)
    #print(count)
    ind=chars.index(i)
    if freq[ind]==0:
        freq[ind]=count
print (freq)

new=[]
chars1=[]
while freq:
    maxi=freq[0]
    for i in freq:
        if i>maxi:
            maxi=i
    c=freq.index(maxi)
    new.append(maxi)
    chars1.append(chars[c])
    chars.remove(chars[c])
    freq.remove(maxi)
print("Table after sorting :")
print(new)   
print(chars1)  

leaves = 0
for x in new:
    if x != 0:
        leaves=leaves+1
nodes = 2*leaves-1


print("Number of nodes in the tree : ",nodes)
print("Number of leafs in the tree : ",leaves)


encoding=["null"]*leaves
print(encoding)

btree=list(new)
stringtree=list(chars1)

print("Binary tree :",btree)
print("String tree :",stringtree)



for j in range(len(btree)-1,-1,-1):
    left=1000
    right=1000
    leftstrings=""
    rightstrings=""
    for k in range(len(btree)-1,-1,-1):
        if btree[k]<right:
            right=btree[k]
            rightstrings=stringtree[k]
            m=k
    print("Right :",right)
    print("Right string tree :",rightstrings)
            
    for r in rightstrings:
        charInd=chars1.index(r)
        if encoding[charInd]=="null":
            encoding[charInd]="0"
        else:
            encoding[charInd]="0"+encoding[charInd]
            
        
        v = stringtree.index(rightstrings)
        stringtree.pop(v)
        btree.pop(v)
        for i in range(len(btree)-1,-1,-1):

            if btree[i] < left or btree[i] == right:
                    left = btree[i]
                    leftstrings = stringtree[i]
                    z = i
                

        for x in leftstrings:
            charInd = chars1.index(x)
            if encoding[charInd]=="null":
                encoding[charInd]="1"
            else:
                encoding[charInd]="1"+encoding[charInd]


        
        w = stringtree.index(leftstrings)
        stringtree.pop(w)
        btree.pop(w)

        sum_ = right + left
        strsum = leftstrings + rightstrings
        stringtree.insert(0,strsum)
        btree.insert(0,sum_)


        print ("value table : ",btree)
        print ("String list : ",stringtree)
        print("encoding : ",encoding)
        if len(btree)==1:
            break
    print ("char : ",chars1)
    f.close()
    chars = ""
    for i in s:
        for j in chars1:
            if j==i:
                p = chars1.index(j)
                chars = chars + encoding[p]

    print (chars)
    
    g = open("output.txt","w")
    g.write(chars)
    g.close()
    p = open("dictionary.txt","w")

    for i in range (0,len(encoding),1):
        length = chars1[i]
        chars = encoding[i]
        w=length+"="+chars
        print (w)
        p.write(w +"\n")
        w = ""
    p.close()
  
