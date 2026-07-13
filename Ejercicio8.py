Grafo= {
    "Houston": ["San Antonio", "Dallas", "Austin"],
    "San Antonio": ["Houston", "Austin", "El Paso"],
    "Dallas": ["Houston", "El Paso"],
    "Austin": ["San Antonio", "Houston", "Dallas", "El Paso"],
    "El Paso": ["San Antonio", "Dallas", "Austin"]

}
print(" Rutas (Grafo No Dirigido) ---")
for ciudad, conexion in Grafo.items():
    print(f"\n{ciudad} está conectada con: {', '.join(conexion)}")

inicio = "Houston"
final = "El Paso"
ruta = ["Houston", "Dallas", "El Paso"]

print(f"\nRuta entre {inicio} a {final}")
print(f"\nRuta encontrada: {' > '.join(ruta)}")