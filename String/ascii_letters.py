import string
result=string.ascii_letters
print(result)

def chack(value):
    for latter in value:
        if latter  not in string.ascii_letters:
            return False
        return True
input1="geeksforgeeks"
print("input is-->",chack(input1))
input2="geeks for geeks"
print("input2-->",chack(input2))
input3="geeks_for_geeks"
print("input3-->",chack(input3))