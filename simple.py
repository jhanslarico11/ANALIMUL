import matplotlib.pyplot as plt

# Datos de ventas de los últimos 5 meses
ventas = [100, 120, 130, 110, 150]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

# Paso 1: Calcular la suma de las ventas
suma_ventas = sum(ventas)

# Paso 2: Calcular el número de observaciones
num_observaciones = len(ventas)

# Paso 3: Calcular el promedio
promedio = suma_ventas / num_observaciones

# Paso 4: Pronóstico para el próximo mes
pronostico = promedio

# Añadir el pronóstico a los datos
meses.append('Junio')
ventas.append(pronostico)

# Mostrar resultados
print("Ventas de los últimos 5 meses:", ventas[:-1])  # Sin incluir el pronóstico
print("Pronóstico para el próximo mes:", pronostico)

# Paso 5: Crear el gráfico
plt.figure(figsize=(10, 5))
plt.plot(meses[:-1], ventas[:-1], marker='o', label='Ventas Históricas', color='blue')
plt.plot(meses[-1], pronostico, marker='o', label='Pronóstico', color='orange')

# Configurar el gráfico
plt.title('Pronóstico de Ventas')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
