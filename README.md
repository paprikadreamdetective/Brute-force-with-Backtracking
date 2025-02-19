# Cifrado y Descifrado de Vigenère

## Definición Matemática

El cifrado de Vigenère es un cifrado polialfabético que utiliza una clave repetitiva para modificar cada letra del texto original.

### 🔹 Cifrado:
Sea:
- $T_i$ el carácter $i$-ésimo del texto en claro.
- $K_i$ el carácter $i$-ésimo de la clave repetida hasta coincidir con la longitud del texto.
- $C_i$ el carácter $i$-ésimo del texto cifrado.
- $A = 0, B = 1, C = 2, ..., Z = 25$ (asignación numérica de las letras).

El cifrado se define como:

$
C_i = (T_i + K_i) \mod 26
$

### 🔹 Descifrado:
Para recuperar el texto original, se usa la operación inversa:

$
T_i = (C_i - K_i + 26) \mod 26
$

Donde $+26$ se usa para evitar valores negativos antes de aplicar el módulo.

### 🔹 Ejemplo de Aplicación:
Si queremos cifrar el texto **"TEXTO"** con la clave **"CLAVE"**, primero convertimos cada letra a su valor numérico:

| Letra Texto | Letra Clave | $T_i$ | $K_i$ | Cifrado $C_i = (T_i + K_i) \mod 26$ | Letra Cifrada |
|-------------|------------|-----------|-----------|----------------------------------|---------------|
| T (19)      | C (2)      | 19        | 2         | (19 + 2) mod 26 = 21            | V             |
| E (4)       | L (11)     | 4         | 11        | (4 + 11) mod 26 = 15            | P             |
| X (23)      | A (0)      | 23        | 0         | (23 + 0) mod 26 = 23            | X             |
| T (19)      | V (21)     | 19        | 21        | (19 + 21) mod 26 = 14           | O             |
| O (14)      | E (4)      | 14        | 4         | (14 + 4) mod 26 = 18            | S             |

Texto cifrado resultante: **"VPXOS"**.

Para descifrar, usamos la ecuación del descifrado y recuperamos el mensaje original.
