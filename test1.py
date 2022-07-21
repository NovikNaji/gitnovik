
inputText=list(input().lower())

lenText=len(inputText)
k=0
outputText=''


for i in range(lenText):
    k=0
    for j in range(lenText):
        if(inputText[i]==inputText[j]):
            k+=1
    if(k==1):
        outputText+='('
    else:
        outputText+=')'

print(outputText)
print(inputText)