from cifrado_vigenere import CifradoVigenere
import itertools

def backtracking(alfabeto, sol, n, level, cifrado, cifrado_vigenere):
    if n < level:
        for letra in alfabeto:
            sol[n] = letra
            backtracking(alfabeto, sol, n+1, level, cifrado, cifrado_vigenere)
    else:
        clave = "".join(sol)
        descifrado = cifrado_vigenere.descifrar(cifrado, clave)
        print(f"Probando clave: {clave} → Mensaje: {descifrado}")
        if descifrado == "TEXTO":
            print("Se encontro la clave")
            exit()

def main():
    cifrado = "VPXOS"  # Fragmento del mensaje cifrado
    longitud_clave = 5  # Se asume que sabemos la longitud de la clave
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras mayúsculas como claves posibles
    solucion = ["A"] * longitud_clave  # Inicializar la clave con 'A'
    cifrado_vigenere = CifradoVigenere()
    print("Iniciando ataque por fuerza bruta con backtracking...")
    #print(descifrar_vigenere(cifrado, "CLAVE"))
    backtracking(alfabeto, solucion, 0, longitud_clave, cifrado, cifrado_vigenere)

if __name__ == "__main__":
    main()
