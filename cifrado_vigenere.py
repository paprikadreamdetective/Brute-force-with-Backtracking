class CifradoVigenere:
    def __init__(self) -> None:
        _text = ''
        _true_key = ''

    def cifrar(self, texto: str, clave: str):
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

    def descifrar(self, cifrado: str, clave: str):
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
