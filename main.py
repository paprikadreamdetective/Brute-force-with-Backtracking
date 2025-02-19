from cifrado_vigenere import CifradoVigenere
from backtraking import backtracking

def main():
    cifrado = "VPXOS"  
    longitud_clave = 5 
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    solucion = ["A"] * longitud_clave  # Inicializar la clave con 'A'
    cifrado_vigenere = CifradoVigenere()
    print("Iniciando ataque por fuerza bruta con backtracking...")
    backtracking(alfabeto, solucion, 0, longitud_clave, cifrado, cifrado_vigenere)

if __name__ == "__main__":
    main()