from datatime import datetime

# Lista de vuelos (simulado)
vuelos_lista = [
  {"id": 1, "origen": "Iquique", "destino": "Santiago", "fecha": "2024-09-12"},
  {"id": 2, "origen": "Santiago", "destino": "Iquique", "fecha": "2024-10-20"}, 
]

# Función para buscar vuelos con parámetros origen, destino, 
# fecha_inicio (inicio rango de búsqueda) y fecha_termino (termino rango de búsqueda)
def buscar_vuelos(origen, destino, fecha_inicio, fecha_termino):
  """
  Busca vuelos basados en origen, destino y en un rango de fechas.
  """
  # Se convierten fechas a objetos datetime para realizar la comparación
  fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
  fecha_termino = datetime.strptime(fecha_termino, '%Y-%m-%d')
  
  return [
    vuelo for vuelo in vuelos
    if (vuelo["origen"] == origen and
        vuelo["destino"] == destino and
       fecha_inicio <= datetime.strptime(vuelo["fecha"], '%Y-%m-%d') <= fecha_termino)                           
  ]

# Ejemplo de uso
origen = "Iquique"
destino = "Santiago"
fecha_inicio = "2024-09-10"
fecha_termino = "2024-09-20"
  
resultados = buscar_vuelos(origen, destino, fecha_inicio, fecha_termino)
print("Vuelos disponibles:")
for vuelo in resultados:
    print(f"ID: {vuelo['id']}, Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Fecha: {vuelo['fecha']}")

  
