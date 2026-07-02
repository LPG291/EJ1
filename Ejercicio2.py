
historial = []

historial.append("google.com")
print("google.com")

historial.append("youtube.com")
print("youtube.com")

historial.append("github.com")
print("github.com")

historial.append("wikipedia.org")
print("wikipedia.org")

print(f"historial: {historial}")

print("Atrás ")
pagina_eliminada = historial.pop()
print(f"Saliendo de: {pagina_eliminada}")

pagina_actual = historial[-1]
print(f"Página actual: {pagina_actual}")

print(f"historial: {historial}")