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


$C_i = (T_i + K_i) \mod 26$


### 🔹 Descifrado:
Para recuperar el texto original, se usa la operación inversa:


$T_i = (C_i - K_i + 26) \mod 26$


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

# Algoritmo de Backtracking

## Definición Matemática

El **backtracking** es una técnica de búsqueda en la cual se exploran todas las soluciones posibles de un problema de manera recursiva, retrocediendo cuando se detecta que una solución parcial no puede conducir a una solución válida.

El algoritmo sigue una estructura general:

1. Si se ha encontrado una solución válida, se almacena o retorna.
2. Si la solución parcial no es válida, se retrocede (**backtrack**).
3. Se prueban todas las opciones posibles desde el estado actual.
4. Se avanza recursivamente con cada opción y se repite el proceso.

Podemos representar el **backtracking** de manera formal con una función recursiva:

$$
\text{Backtrack}(sol, n) =
\begin{cases} 
\text{Procesar solución si es válida}, & \text{si } n \text{ es una solución completa} \\
\text{Para cada opción posible:} & \\
\quad \text{Agregar opción a } sol & \\
\quad \text{Llamar recursivamente a } \text{Backtrack}(sol, n+1) & \\
\quad \text{Eliminar opción y retroceder} & 
\end{cases}
$$

---

## Ejemplo: Generación de Claves con Backtracking

Imaginemos que queremos generar todas las combinaciones posibles de una clave de longitud $L$ utilizando un alfabeto $\Sigma$ con $N$ caracteres. Podemos hacerlo con backtracking probando cada combinación de letras.

### Algoritmo:
1. Se define un conjunto de caracteres posibles $\Sigma = \{A, B, C, ..., Z\}$.
2. Se construye una clave de longitud $L$, probando todas las combinaciones posibles.
3. Si la clave alcanza la longitud deseada, se prueba su validez.
4. Si la clave no es correcta, se retrocede y se intenta una nueva combinación.

El número total de combinaciones generadas es:

$$
|\Sigma|^L = N^L
$$

Si $|\Sigma| = 26$ (alfabeto en inglés) y la clave tiene longitud $L = 5$, entonces hay:

$$
26^5 = 11,881,376
$$

posibles claves que deben probarse.


