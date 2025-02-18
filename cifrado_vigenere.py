def cifrar_vigenere(texto, clave):
    texto = texto.upper()  # Convertimos todo a mayúsculas
    clave = clave.upper()
    texto_len = len(texto)
    clave_len = len(clave)
    
    nueva_clave = ""  # Generar la clave extendida
    for i in range(texto_len):
        nueva_clave += clave[i % clave_len]
    
    cifrado_texto = ""
    for i in range(texto_len):
        cifrado_texto += chr(((ord(texto[i]) + ord(nueva_clave[i]) - 2 * ord('A')) % 26) + ord('A'))
    
    print("Texto cifrado:", cifrado_texto)

# Prueba con los mismos datos
texto = "HOLA"
clave = "CLAVE"
cifrar_vigenere(texto, clave)
