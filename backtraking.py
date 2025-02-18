import itertools

# Función para descifrar con la clave dada
def descifrar_vigenere(cifrado, clave):
    cifrado = cifrado.upper()
    clave = clave.upper()
    texto_len = len(cifrado)
    clave_len = len(clave)
    
    nueva_clave = ""
    for i in range(texto_len):
        nueva_clave += clave[i % clave_len]
    
    texto_descifrado = ""
    for i in range(texto_len):
        texto_descifrado += chr(((ord(cifrado[i]) - ord(nueva_clave[i]) + 26) % 26) + ord('A'))
    


    return texto_descifrado

# Backtracking para generar claves y probarlas
def backtracking(alfabeto, sol, n, level, cifrado):
    if n < level:
        for letra in alfabeto:
            sol[n] = letra
            backtracking(alfabeto, sol, n+1, level, cifrado)
    else:
        clave = "".join(sol)
        descifrado = descifrar_vigenere(cifrado, clave)
        print(f"Probando clave: {clave} → Mensaje: {descifrado}")
        if descifrado == "TEXTO":
            print("Se encontro la clave")
            exit()

def main():
    cifrado = "VPXOS"  # Fragmento del mensaje cifrado
    longitud_clave = 5  # Se asume que sabemos la longitud de la clave
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras mayúsculas como claves posibles
    solucion = ["A"] * longitud_clave  # Inicializar la clave con 'A'
    
    print("Iniciando ataque por fuerza bruta con backtracking...")
    #print(descifrar_vigenere(cifrado, "CLAVE"))
    backtracking(alfabeto, solucion, 0, longitud_clave, cifrado)

if __name__ == "__main__":
    main()
