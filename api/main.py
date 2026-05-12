from fastapi import FastAPI, Depends

app = FastAPI(title="NYC TLC API Gateway")

@app.get("/")
def read_root():
    return {"status": "Sistema NYC TLC Operativo", "arquitectura": "Lakehouse"}

# Simulación de seguridad OAuth2 mencionada en el informe
@app.get("/fiscalizadores/reportes")
def get_reports():
    return {"mensaje": "Acceso autorizado para fiscalización", "data": "Reporte Mensual Abril 2026"}