import random
def gen_passcode(num:int=4):
    """
    the function to genrate password verification email code
    
    :param_1 : take length of code in num variables input user interface
    type param_1 : int 
    
    return : str
    """
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password=""
    length=num
    for _ in range (length) :
        password += random.choice(characters)

    print(f"Generated Password : {password}")
