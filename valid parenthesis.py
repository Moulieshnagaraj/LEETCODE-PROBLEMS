
dict = {
    ")":"(",
    "}":"{",
    "]":"["
}
str1="({)}"
li=[]
for i in str1:
    if i in dict:
        li.pop()
    else:
        li.append(i)
if li:
    print(False)
else:
    print(True)
