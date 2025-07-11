def main():
    entrada = input("Ingresa el número de VLAN (1–4094): ").strip()

    vlan = int(entrada)
    if 1 <= vlan <= 1005:
        rango = "normal"
    elif 1006 <= vlan <= 4094:
        rango = "extendido"
    else:
        print(f"{vlan} no es un número de VLAN válido (debe estar entre 1 y 4094).")
        return

    print(f"La VLAN {vlan} corresponde al rango **{rango}**.")

if __name__ == "__main__":
    main()