import os
import hashlib

def getHash(irudia):
    md5 = hashlib.md5()
    with open(irudia, "rb") as img:
        while True:
            hashInfo = img.read(65536)
            if not hashInfo:
                break
            md5.update(hashInfo)
    return md5.hexdigest()

hashBilatu = "e5ed313192776744b9b93b1320b5e268" #HEMEN IDATZI BILATU NAHI DEN HASH-A

fitxategi = "/home/oierur05/Downloads/irudia/" #HEMEN IDATZI FITXATEGIEN KOKAPENA

for irudia in os.listdir(fitxategi):
    helb = os.path.join(fitxategi, irudia)
    if os.path.isfile(helb):
        hashImg = getHash(helb)
        if hashImg == hashBilatu:
            print(f"Hash: {irudia}")
            break
else:
    print("Hash-a ez da aurkitu")