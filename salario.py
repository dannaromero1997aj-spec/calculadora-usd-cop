import requests

def obtener_trm():
    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = r.json()
        trm = data['rates']['COP']
        return trm
    except:
        print("No pude traer la TRM, usando 4200 por defecto")
        return 4200

def calcular_salario():
    print("=== CALCULADORA USD -> COP ===")
    salario_usd_anual = float(input("Cuanto ganas al año en USD? Ej: 100000: "))
    trm = obtener_trm()
    print(f"\nTRM de hoy: ${trm:,.2f} COP")
    anual_cop = salario_usd_anual * trm
    mensual_cop = anual_cop / 12
    quincenal_cop = anual_cop / 24
    print(f"\n--- RESULTADOS ---")
    print(f"Anual: ${anual_cop:,.0f} COP")
    print(f"Mensual: ${mensual_cop:,.0f} COP")
    print(f"Quincenal: ${quincenal_cop:,.0f} COP")
    salario_min_2026 = 1423500
    cuantos_minimos = mensual_cop / salario_min_2026
    print(f"\nEso son {cuantos_minimos:.1f} salarios minimos de Colombia")

if __name__ == "__main__":
    calcular_salario()