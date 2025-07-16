# reto-11
1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

| Método        | Descripción                                                                 | Ejemplo                       | Resultado |
|---------------|------------------------------------------------------------------------------|-------------------------------|-----------|
| `endswith()`  | Verifica si la cadena termina con un sufijo específico.                    | `"python".endswith("on")`     | `True`    |
| `startswith()`| Verifica si la cadena comienza con un prefijo específico.                  | `"python".startswith("py")`   | `True`    |
| `isalpha()`   | Retorna `True` si todos los caracteres son letras.                         | `"Hola".isalpha()`            | `True`    |
| `isalnum()`   | Retorna `True` si todos los caracteres son alfanuméricos (letras o números).| `"Hola123".isalnum()`         | `True`    |
| `isdigit()`   | Retorna `True` si todos los caracteres son dígitos.                        | `"123".isdigit()`             | `True`    |
| `isspace()`   | Retorna `True` si todos los caracteres son espacios en blanco.             | `"   ".isspace()`             | `True`    |
| `istitle()`   | Retorna `True` si la cadena está en formato título (cada palabra capitalizada).| `"Hola Mundo".istitle()`   | `True`    |
| `islower()`   | Retorna `True` si todos los caracteres alfabéticos están en minúsculas.    | `"python".islower()`          | `True`    |
| `isupper()`   | Retorna `True` si todos los caracteres alfabéticos están en mayúsculas.    | `"PYTHON".isupper()`          | `True`    |
2. Procesar el archivo y extraer:
+ Cantidad de vocales
+ Cantidad de consonantes
+ Listado de las 50 palabras que mas se repiten
+ Para este punto se utilizo el programa adjunto como "reto11.py"

### resultados ###
+ Análisis de archivo mbox.txt
+ Cantidad de vocales: 1597835
+ Cantidad de consonantes: 2612121
+ Top 50 palabras más frecuentes:
+ edu: 31260
+ org: 22456
+ sakaiproject: 21747
+ from: 21721
+ by: 18028
+ collab: 17970
+ x: 16677
+ received: 16176
+ iupui: 14820
+ umich: 14724
+ src: 14622
+ id: 14408
+ ac: 14260
+ uk: 13874
+ source: 13306
+ with: 12757
+ uhi: 12579
+ nakamura: 12571
+ uits: 12571
+ content: 12130
+ java: 11336
+ branches: 10422
+ tool: 10030
+ dec: 9267
+ sak: 9220
+ nov: 8988
+ for: 7715
+ impl: 7672
+ mail: 7207
+ esmtp: 7188
+ paploo: 7188
+ dspam: 7188
+ message: 5507
+ text: 5423
+ type: 5418
+ utf: 5394
+ mr: 5391
+ itd: 5391
+ localhost: 5391
+ plain: 5391
+ charset: 5391
+ webapp: 5282
+ gmt: 5021
+ trunk: 4986
+ rwiki: 4969
+ thu: 4783
+ to: 4569
+ tue: 4502
+ sakai: 4470
+ oct: 4164
