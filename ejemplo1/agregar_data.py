import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

lista_datos = []

with open('saludos_mundo.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')  
    for row in reader:
        print(row)  
        saludo = Saludo2(
            mensaje=row['saludo'], 
            tipo=row['tipo'],
            origen=row['origen']
        )
        lista_datos.append(saludo)

print(f"📦 Datos cargados desde el CSV: {len(lista_datos)} registros")

session.add_all(lista_datos)
session.commit()

print("✅ Datos insertados correctamente en la base de datos.")
