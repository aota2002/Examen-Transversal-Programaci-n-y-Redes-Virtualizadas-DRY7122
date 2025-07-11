#!/usr/bin/env python3
# travel_distance.py
# Requiere: geopy (pip3 install geopy)

from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import sys

# Velocidades promedio (km/h) según medio de transporte
SPEEDS_KMH = {
    '1': ('Auto', 80),
    '2': ('Tren', 100),
    '3': ('Avión', 800),
    '4': ('Bicicleta', 15),
}

def get_coordinates(ciudad, pais):
    """Geocodifica ciudad con el país indicado."""
    geolocator = Nominatim(user_agent="travel_app")
    loc = geolocator.geocode(f"{ciudad}, {pais}")
    if not loc:
        return None
    return (loc.latitude, loc.longitude)

def formato_tiempo(hours):
    h = int(hours)
    m = int(round((hours - h) * 60))
    return f"{h} h {m} min"

def main():
    print("=== Calculadora de distancia y tiempo de viaje ===")
    while True:
        origen = input("Ciudad de Origen (en Chile) [o 's' para salir]: ").strip()
        if origen.lower() == 's':
            print("¡Hasta luego!")
            sys.exit(0)

        destino = input("Ciudad de Destino (en Argentina) [o 's' para salir]: ").strip()
        if destino.lower() == 's':
            print("¡Hasta luego!")
            sys.exit(0)

        coord_o = get_coordinates(origen, "Chile")
        coord_d = get_coordinates(destino, "Argentina")
        if not coord_o or not coord_d:
            print("❌ No pude encontrar alguna de las ciudades. Revisa la ortografía e inténtalo de nuevo.\n")
            continue

        dist_km = great_circle(coord_o, coord_d).kilometers
        dist_mi = great_circle(coord_o, coord_d).miles

        print("\nMedios de transporte:")
        for k,(n,_) in SPEEDS_KMH.items():
            print(f" {k}. {n}")
        medio = input("Opción (1–4) o 's' para salir: ").strip()
        if medio.lower() == 's':
            print("¡Hasta luego!")
            sys.exit(0)
        if medio not in SPEEDS_KMH:
            print("❌ Opción inválida. Intenta de nuevo.\n")
            continue

        medio_name, speed = SPEEDS_KMH[medio]
        tiempo_h = dist_km / speed
        tiempo_str = formato_tiempo(tiempo_h)

        print("\n--- Resultado del viaje ---")
        print(f"Origen     : {origen}, Chile")
        print(f"Destino    : {destino}, Argentina")
        print(f"Distancia  : {dist_km:.2f} km  ({dist_mi:.2f} millas)")
        print(f"Medio      : {medio_name}")
        print(f"Duración   : {tiempo_str}\n")

        print("Narrativa:")
        print(f"Partirás de {origen} (Chile) en {medio_name.lower()} a ~{speed} km/h, "
              f"recorriendo {dist_km:.0f} km ({dist_mi:.0f} mi) hasta {destino} "
              f"en aproximadamente {tiempo_str}.\n")

        if input("¿Calcular otro viaje? (s para sí): ").lower() != 's':
            print("¡Fin del programa!")
            break

if __name__ == "__main__":
    main()
