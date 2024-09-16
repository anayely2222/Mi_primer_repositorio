#Hacer matriz 3D que represente datos de temperaturas , en este caso de las ciudades Orellana, Santa Elena y Carchi
# Definir los parámetros
temperaturas =[
    [#Orellana
        [#semana1

            {"dia":"lunes","tempera":35},
            {"dia":"Martes","tempera":32},
            {"dia":"Miercoles","tempera":35},
            {"dia":"Jueves","tempera":33},
            {"dia":"Sabado","tempera":34},
            {"dia":"Domingo","tempera":32}
        ],
        [#semana2

            {"dia":"lunes","tempera":36},
            {"dia":"Martes","tempera":32},
            {"dia":"Miercoles","tempera":38},
            {"dia":"Jueves","tempera":33},
            {"dia":"Sabado","tempera":33},
            {"dia":"Domingo","tempera":32}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 32},
            {"dia": "Martes", "tempera": 33},
            {"dia": "Miercoles", "tempera": 35},
            {"dia": "Jueves", "tempera": 37},
            {"dia": "Sabado", "tempera": 33},
            {"dia": "Domingo", "tempera": 32}
        ],
        [#semana4
            {"dia": "lunes", "tempera": 30},
            {"dia": "Martes", "tempera": 32},
            {"dia": "Miercoles", "tempera": 29},
            {"dia": "Jueves", "tempera": 31},
            {"dia": "Sabado", "tempera": 34},
            {"dia": "Domingo", "tempera": 32}
        ]
         ],
    [#Santa Elena
        [#semana1
            {"dia": "lunes", "tempera": 22},
            {"dia": "Martes", "tempera": 27},
            {"dia": "Miercoles", "tempera": 25},
            {"dia": "Jueves", "tempera": 23},
            {"dia": "Sabado", "tempera": 22},
            {"dia": "Domingo", "tempera": 26}
        ],
        [#semana2
            {"dia": "lunes", "tempera": 25},
            {"dia": "Martes", "tempera": 23},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 23},
            {"dia": "Sabado", "tempera": 23},
            {"dia": "Domingo", "tempera": 22}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 35},
            {"dia": "Martes", "tempera": 32},
            {"dia": "Miercoles", "tempera": 35},
            {"dia": "Jueves", "tempera": 33},
            {"dia": "Sabado", "tempera": 34},
            {"dia": "Domingo", "tempera": 32}
        ],

        [#semana4
            {"dia": "lunes", "tempera": 25},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 25},
            {"dia": "Jueves", "tempera": 26},
            {"dia": "Sabado", "tempera": 26},
            {"dia": "Domingo", "tempera": 25}
        ]

    ],
    [#Carchi
        [#semana1
            {"dia": "lunes", "tempera": 15},
            {"dia": "Martes", "tempera": 18},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 21},
            {"dia": "Sabado", "tempera": 21},
            {"dia": "Domingo", "tempera": 19}
        ],
        [#semana2
            {"dia": "lunes", "tempera": 16},
            {"dia": "Martes", "tempera": 21},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 18},
            {"dia": "Sabado", "tempera": 16},
            {"dia": "Domingo", "tempera": 18}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 19},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 21},
            {"dia": "Jueves", "tempera": 20},
            {"dia": "Sabado", "tempera": 19},
            {"dia": "Domingo", "tempera": 18}
        ],
        [#Semana4
            {"dia": "lunes", "tempera": 21},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 19},
            {"dia": "Sabado", "tempera": 19},
            {"dia": "Domingo", "tempera": 22}
        ]
    ]
]
#Se calcula el promedio de cada semana y ciudad
ciudades = ["Orellana", "Santa Elena", "Carchi"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_tempera = sum([dia["tempera"] for dia in semana])
        promedio = suma_tempera / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")