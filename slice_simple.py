def slice_simple():
    texto = "Awesome"
    texto=texto.lower()
    print (texto[:3])
    print(texto[int(len(texto)/2)-1 :int(len(texto)/2) +2 ])
    print(texto[:4]+texto[len(texto)-3:])
slice_simple()
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
