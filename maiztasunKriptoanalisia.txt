def deszifratu(mezua):
    
    hitzak = mezua.split()
    
    arrayLetra = {}
    for h in hitzak:
        for l in h:
            if l.isalpha():
                if l in arrayLetra:
                    arrayLetra[l] += 1
                else:
                    arrayLetra[l] = 1
    print(arrayLetra)
    listaOrd = sorted(arrayLetra, key = arrayLetra.get, reverse = True)
    print(listaOrd)
    z,b = input("Adierazi zein letra aldatu nahi dituzun:\n").split()
    i = 0
    while z != 'fin':
        ordezkatua = listaOrd.index(z.upper())
        if i == 0:
            mezuDeszifratua = mezua.replace(listaOrd[ordezkatua],b)
        else:
            mezuDeszifratua = mezuDeszifratua.replace(listaOrd[ordezkatua],b)
        
        print(mezuDeszifratua)
        i += 1
        z,b = input("Adierazi zein letra aldatu nahi dituzun:\n").split()
        

if __name__ == "__main__":            
   
    mezua = '''
    IDATZI HEMEN DESZIFRATZEKO MEZUA
'''

    deszifratu(mezua)    
    
