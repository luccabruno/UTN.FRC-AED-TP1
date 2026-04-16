# 1 Paciente.
paciente = input()

# 2 Código de enfermedad.
codigo = input() # Ejemplo A02.3
letra = codigo[0] # "A"
numero = codigo[1:3] # "02"
sub = codigo[4:] # "3"

# 3 Descripción del código de enfermedad y capítulo al que pertenece.
if letra in {"A", "B"}:
    capitulo = "Enfermedades infecciosas y parasitarias"
elif letra in {"C"}:
    capitulo = "Neoplasias"
elif letra in {"D"}:
    if "00" <= numero <= "48":
        capitulo = "Neoplasias"
    elif "50" <= numero <= "89":
        capitulo = "Enfermedades de la sangre y de los órganos hematopoyéticos y ciertos trastornos que afectan el mecanismo de defensa del organismo"
elif letra in {"E"}:
    capitulo = "Enfermedades endocrinas, nutricionales y metabólicas"
elif letra in {"F"}:
    capitulo = "Trastornos mentales y del comportamiento"
elif letra in {"G"}:
    capitulo = "Enfermedades del sistema nervioso"
elif letra in {"H"}:
    if "00" <= numero <= "59":
        capitulo = "Enfermedades del ojo y sus anexos"
    elif "60" <= numero <= "95":
        capitulo = "Enfermedades del oído y de la apófisis mastoides"
elif letra in {"I"}:
    capitulo = "Enfermedades del sistema circulatorio"
elif letra in {"J"}:
    capitulo = "Enfermedades del sistema respiratorio"
elif letra in {"K"}:
    capitulo = "Enfermedades del sistema digestivo"
elif letra in {"L"}:
    capitulo = "Enfermedades de la piel y del tejido subcutáneo"
elif letra in {"M"}:
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conectivo"
elif letra in {"N"}:
    capitulo = "Enfermedades del sistema genitourinario"
elif letra in {"O"}:
    capitulo = "Embarazo, parto y puerperio"
elif letra in {"P"}:
    capitulo = "Ciertas afecciones originadas en el período perinatal"
elif letra in {"Q"}:
    capitulo = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
elif letra in {"R"}:
    capitulo = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
elif letra in {"S", "T"}:
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif letra in {"V", "W", "X", "Y"}:
    capitulo = "Causas externas de morbilidad y mortalidad"
elif letra in {"Z"}:
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra in {"U"}:
    capitulo = "Códigos especiales para situaciones que no se pueden clasificar en otra parte"

# 4 Cálculo de monto a pagar.
monto_base = int(input())
monto_fijo = monto_base + 25000
total = monto_fijo
if "A" <= letra <= "L":
    total = monto_fijo + 25000
elif "M" <= letra <= "Z" and letra != "U":
    total = monto_fijo + 40000
elif letra == "U":
    total = monto_fijo + 100000

#5 Aplicar porcentaje.
porcentaje = int(sub)
total = total + (porcentaje / 100) * total

# 6 Consigna extra que falta que nos den.

# 7 Imprimir el resultado.
print("Beneficiario:", paciente)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", total)
