# AED TP1 - Sistema de Gestión de Tratamientos Médicos

## Descripción del Proyecto
Este repositorio contiene el código fuente correspondiente al Trabajo Práctico 1 de la asignatura Algoritmos y Estructuras de Datos (Ciclo 2026). El proyecto consiste en un programa desarrollado en Python encargado de procesar y facturar tratamientos médicos de un centro de salud.

El sistema basa su lógica de identificación de problemas de salud en el formato de códigos ICD10 (International Classification of Diseases, versión 10 de la OMS).

## Estructura de Datos
El script trabaja procesando un único tratamiento a la vez, recibiendo la siguiente información por teclado:

- Nombre del paciente: Cadena de caracteres que incluye nombre y apellido.
- Código ICD10: Cadena alfanumérica que representa el diagnóstico médico. El formato estándar esperado es X##.## (una letra indicando el grupo, dos dígitos indicando el bloque, un punto, y uno o dos dígitos indicando el problema específico).
- Monto base: Número entero que representa el costo inicial del tratamiento.

## Lógica de Facturación
El programa (.py) aplica una serie de reglas secuenciales para calcular el costo final a cobrarle al paciente:

1. Cargo Fijo: Se adicionan $25000 al monto base en todos los casos.
2. Cargo por Grupo de Enfermedad (Letra inicial):
- Si la letra está entre "A" y "L": se suman $25000 adicionales.
- Si la letra está entre "M" y "Z" (excepto "U"): se suman $40000 adicionales.
- Si la letra es "U" (códigos especiales): se suman $100000 adicionales.
3. Porcentaje Específico: Al subtotal obtenido se le aplica un recargo porcentual. Este porcentaje equivale exactamente al número que se encuentra a la derecha del punto en el código ICD10 ingresado.

## Salidas y Formato Estricto
La corrección del trabajo se realiza de manera semiautomática mediante un programa evaluador (runner). Por este motivo, el código está diseñado con una política estricta de Entradas/Salidas:

- Sin interacciones extra: El script no imprime mensajes de bienvenida, no pide confirmaciones, ni agrega texto descriptivo al momento de solicitar los datos de entrada (se respeta el orden estricto de carga).
- Formato de impresión: Los resultados se imprimen exactamente con la siguiente estructura:

Beneficiario: [Nombre del paciente cargado]
Codigo: [Código ICD10 cargado]
Capitulo: [Nombre del capítulo de la OMS correspondiente al código]
Monto a pagar: [Cálculo matemático final]

### Notas de Desarrollo
- Mapeo de Capítulos: Una parte fundamental de la lógica interna del script es la evaluación de los prefijos del código ICD10 para determinar y devolver el nombre en texto claro de uno de los 22 capítulos del catálogo.
- Actualización en Laboratorio: El script actual representa el Enunciado Base. Durante la semana del 20 al 24 de abril, se realizará un commit adicional resolviendo un requerimiento extra que será dictado presencialmente en clases.
