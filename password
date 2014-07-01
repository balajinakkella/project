#Password validation function in python
#driver function passwordval(string)

primary_error="Passwords must have at least 8 characters and contain at least two of the following: uppercase letters, lowercase letters, numbers, and symbols."
invalid_error="Password must contain a-z A-Z 0-9 and .!#$%&'+/=?[]^`{|}~"
def islower(x):
    return x in "abcdefghijklmnopqrstuvwxyz"

def isupper(x):
    return x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def isnumber(x):
    return x in "1234567890"

def issymbol(x):
    return x in ".!#$%&'+/=?[]^`{|}~"

def passwordval(password):
    length=len(password)
    clower=0
    cnumber=0
    cupper=0
    csymbol=0
    
    if length >= 8:#atleast 8 characters

        #checking that characters in entered password matches with characters in b
        b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.!#$%&'+/=?[]^`{|}~"
        sb=set(b)
        sa=set(password)
        y = not sa.issubset(sb)
        if y:
            return invalid_error
        for i in password:
            if islower(i):
                clower+=1
            elif isupper(i):
                cupper+=1
            elif isnumber(i):
                cnumber+=1
            else:
                csymbol+=1

        if csymbol>1:
            if cnumber>1:
                if cupper>1:
                    if clower>1:
                        return "Strong Password"
                    else:
                        return "atleast 1 lowercase alphabet"
                else:
                    return "atleast 1 uppercase alphabet"
            else:
                return "atleast 1 number"
        else:
            return "atleast 1 special symbol .!#$%&'+/=?[]^`{|}~"
    else:
        return primary_error

