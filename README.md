# 🔐Password Auditor (Local & Ético)

Herramienta sencilla en **Python** para analizar la fortaleza de contraseñas **localmente**,
sin enviar datos a Internet.

Además, evalúa entropía, patrones comunes y ofrece algunas sugerencias para poder mejorar
la seguridad de tus contraseñas.

Cuando menciono el término de entropia, me refiero por ejemplo:
- Medira la dificultad que tendría un cibercriminal para descifrar o adivinar una contraseña.

Cuando se tiende a calcular la entropía de una contraseña, se tiende a tomar en cuenta
la longitud y tambien la variedad de caractéres que esta contiene.



## 👀Características

- Análisis local (sin conexion ni ningún tipo de recoleccion de datos).
- Detección de contraseñas debiles y patrones comúnes.
- Cálculo de entropía.
- Sugerencias personalizadas.
- Compatible con Python 3.8+.


---
## 🔎Ejemplo de Salida

- 🔑Contraseña: admin123
- ❌Fortaleza: Debil.
- 👨‍💻​Sugerencia: Evitar contraseñas comúnes y agrega símbolos o mayúsculas.
<br></br>


- 🔑Contraseña: QwErTy$45
- ➖Fortaleza: Media.
- 👨‍💻Sugerencia: Use al menos 12 caractéres únicos y mezcla números y símbolos.
<br></br>


- 🔑Contraseña: G7b!mXr9T#v2
- ✅Fortaleza: Fuerte.
- 👨‍💻Sugerencia: ¡Excelente! Esta contraseña tiene una buena entropía.


---

## ⚖️Uso Ético

Esta herramienta no debe ser utilizada para auditar contraseñas de otros sistemas
sin el apropiado consentimiento.

Esta diseñada unica y específicamente para el aprendizaje, autoevaluación y en
ayudarte a mejorar la seguridad de tus contraseñas y practicas.
