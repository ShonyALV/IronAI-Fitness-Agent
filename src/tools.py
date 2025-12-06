# src/tools.py

def calculate_bmi_tool(weight_kg: float, height_m: float) -> str:
    """Calcula el BMI y da una clasificación simple."""
    if height_m <= 0: return "Error: Altura inválida."
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)
    
    if bmi < 18.5: status = "Bajo peso"
    elif bmi < 25: status = "Peso normal"
    elif bmi < 30: status = "Sobrepeso"
    else: status = "Obesidad"
    
    return f"BMI Calculado: {bmi} ({status})"
