from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --------- Eingabemodelle ---------
class GGTInput(BaseModel):
    a: int
    b: int

class WurzelInput(BaseModel):
    z: float

# --------- GGT-FUNKTION (aus deinem Code) ---------
def ggt(z1, z2):
    z1 = abs(z1)
    z2 = abs(z2)

    while z2 != 0:
        z1, z2 = z2, z1 % z2
    return z1

# --------- HERON-VERFAHREN (aus deinem Code) ---------
def wurzel_heron(z):
    if z < 0:
        z = abs(z)

    altz = z
    neuz = 0
    while abs(altz - neuz) > 1e-10:
        altz = z
        z = (z + (z / z)) / 2
        neuz = z
    return z

# --------- API-ENDPUNKTE ---------
@app.post("/ggt")
def berechne_ggt(data: GGTInput):
    if data.a == data.b:
        return {"error": "Bitte zwei verschiedene Zahlen eingeben"}
    return {"ggt": ggt(data.a, data.b)}

@app.post("/wurzel")
def berechne_wurzel(data: WurzelInput):
    return {"wurzel": wurzel_heron(data.z)}
