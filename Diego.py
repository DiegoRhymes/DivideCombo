import os

def banner():
    print("=" * 45)
    print("        🔥 DIEGO IPTV 🔥")
    print("     Divisor Profesional de Combos")
    print("=" * 45)

banner()

# Ruta de salida
ruta = "/sdcard/combo"
os.makedirs(ruta, exist_ok=True)

# Archivo de entrada
archivo_entrada = input("📄 Ingresa la ruta el archivo combo (.txt): ").strip()

if not os.path.isfile(archivo_entrada):
    print("❌ El archivo no existe.")
    exit()

# Leer combos
with open(archivo_entrada, "r", encoding="utf-8", errors="ignore") as f:
    combos = f.readlines()

total = len(combos)

if total == 0:
    print("❌ El archivo está vacío.")
    exit()

print(f"\n📦 Total de combos encontrados: {total}")

# Menú
print("\n¿En cuántas partes deseas dividirlo?")
for i in range(1, 6):
    print(f"{i}️⃣  {i} parte(s)")

opcion = input("👉 Selecciona (1-5): ").strip()

if opcion not in ["1", "2", "3", "4", "5"]:
    print("❌ Opción inválida.")
    exit()

partes = int(opcion)
tamano = total // partes

# Nombre base del archivo original
nombre_base = os.path.splitext(os.path.basename(archivo_entrada))[0]

inicio = 0

print("\n📂 Creando divisiones...\n")

for i in range(partes):
    fin = inicio + tamano

    # Última parte se queda con el resto
    if i == partes - 1:
        fin = total

    nombre_salida = f"{nombre_base}_div{i+1}.txt"
    ruta_final = os.path.join(ruta, nombre_salida)

    with open(ruta_final, "w", encoding="utf-8") as f:
        f.writelines(combos[inicio:fin])

    print(f"✅ Div {i+1} → {ruta_final}")
    inicio = fin

print("\n🎉 Proceso completado con éxito")
print("🙌 Gracias por usar DIEGO IPTV")
