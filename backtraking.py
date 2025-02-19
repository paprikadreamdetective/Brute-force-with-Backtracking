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

