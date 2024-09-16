temperaturas =[
    [#Orellana
        [#semana1

            {"dia":"lunes","tempera":35},
            {"dia":"Martes","tempera":32},
            {"dia":"Miercoles","tempera":35},
            {"dia":"Jueves","tempera":33},
            {"dia":"Viernes","tempera":35},
            {"dia":"Sabado","tempera":34},
            {"dia":"Domingo","tempera":32}
        ],
        [#semana2

            {"dia":"lunes","tempera":36},
            {"dia":"Martes","tempera":32},
            {"dia":"Miercoles","tempera":38},
            {"dia":"Jueves","tempera":33},
            {"dia":"Viernes","tempera":35},
            {"dia":"Sabado","tempera":33},
            {"dia":"Domingo","tempera":32}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 32},
            {"dia": "Martes", "tempera": 33},
            {"dia": "Miercoles", "tempera": 35},
            {"dia": "Jueves", "tempera": 37},
            {"dia":"Viernes","tempera":35},
            {"dia": "Sabado", "tempera": 33},
            {"dia": "Domingo", "tempera": 32}
        ],
        [#semana4
            {"dia": "lunes", "tempera": 30},
            {"dia": "Martes", "tempera": 32},
            {"dia": "Miercoles", "tempera": 29},
            {"dia": "Jueves", "tempera": 31},
            {"dia":"Viernes","tempera":35},
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
            {"dia":"Viernes","tempera":25},
            {"dia": "Sabado", "tempera": 22},
            {"dia": "Domingo", "tempera": 26}
        ],
        [#semana2
            {"dia": "lunes", "tempera": 25},
            {"dia": "Martes", "tempera": 23},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 23},
            {"dia":"Viernes","tempera":25},
            {"dia": "Sabado", "tempera": 23},
            {"dia": "Domingo", "tempera": 22}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 35},
            {"dia": "Martes", "tempera": 32},
            {"dia": "Miercoles", "tempera": 35},
            {"dia": "Jueves", "tempera": 33},
            {"dia":"Viernes","tempera":35},
            {"dia": "Sabado", "tempera": 34},
            {"dia": "Domingo", "tempera": 32}
        ],

        [#semana4
            {"dia": "lunes", "tempera": 25},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 25},
            {"dia": "Jueves", "tempera": 26},
            {"dia":"Viernes","tempera":25},
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
            {"dia":"Viernes","tempera":16},
            {"dia": "Sabado", "tempera": 21},
            {"dia": "Domingo", "tempera": 19}
        ],
        [#semana2
            {"dia": "lunes", "tempera": 16},
            {"dia": "Martes", "tempera": 21},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 18},
            {"dia":"Viernes","tempera":20},
            {"dia": "Sabado", "tempera": 16},
            {"dia": "Domingo", "tempera": 18}
        ],
        [#semana3
            {"dia": "lunes", "tempera": 19},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 21},
            {"dia": "Jueves", "tempera": 20},
            {"dia":"Viernes","tempera":25},
            {"dia": "Sabado", "tempera": 19},
            {"dia": "Domingo", "tempera": 18}
        ],
        [#Semana4
            {"dia": "lunes", "tempera": 21},
            {"dia": "Martes", "tempera": 22},
            {"dia": "Miercoles", "tempera": 20},
            {"dia": "Jueves", "tempera": 19},
            {"dia":"Viernes","tempera":22},
            {"dia": "Sabado", "tempera": 19},
            {"dia": "Domingo", "tempera": 22}
        ]
    ]
]
def promedio_temperaturas(datos_tempera, ciudad, semana):
    promedio_tempera=0
    acumulador=0
    for temp in range(len(datos_tempera[ciudad][semana])):
        acumulador= acumulador+datos_tempera[ciudad][semana][temp]
       #acumulador= acumulador+ datos_tempera[ciudad][semana][temp]
    promedio=acumulador/len(datos_tempera[ciudad][semana])
    return promedio

    promedio_temp1 = promedio_temperaturas(temperaturas,ciudad:0,semana:0)
    promedio_temp2 =promedio_temperaturas( temperaturas,ciudad:0,semana:1)
    promedio_temp3 =promedio_temperaturas( temperaturas,ciudad:2,semana:3)

    print(promedio_temp1)
    print(promedio_temp2)
    print(promedio_temp3)


