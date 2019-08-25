""" 
    RC4 Algorithmen: KSA und PRGA
    KSA: Key Scheduling Algorithm
    PRGA: Pseudo Random Number Generator Algorithmus
"""


S_arr=[]
arr_groesse=pow(2,3)

def ksa(key):
    """
        Initialisierung des S_arr[]
    """

    for i in range(arr_groesse):
        S_arr.append(i)
    j=0

    """ 
        Scramble Data
    """ 
    for i in range(arr_groesse):
        j=(j + S_arr[i] +ord(key[i%(len(key))]))%arr_groesse
      
        S_arr[i], S_arr[j]=S_arr[j],S_arr[i]
        print S_arr

    return S_arr




def prga():
    j=0
    i=0
    for n in range(arr_groesse):
        i= (i + 1)%arr_groesse
        j=(j+S_arr[i])%(arr_groesse)
        S_arr[i], S_arr[j] = S_arr[j], S_arr[i]
        print("Wort {}: {}".format(n,S_arr[(S_arr[i]+S_arr[j])%(arr_groesse)]))
        

key = raw_input(">")
print("----------")
ksa(key)
prga()


