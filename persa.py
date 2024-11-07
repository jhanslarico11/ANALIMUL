import numpy as np

# Función de activación (Escalón)
def activacion(x):
    return 1 if x >= 0 else 0

# Perceptrón
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.pesos = np.zeros(input_size)  # Inicializa los pesos a 0
        self.sesgo = 0  # Inicializa el sesgo a 0
        self.learning_rate = learning_rate

    def predecir(self, entradas):
        suma = np.dot(entradas, self.pesos) + self.sesgo
        return activacion(suma)

    def entrenar(self, entradas, etiquetas, epochs=10):
        for _ in range(epochs):
            for x, y in zip(entradas, etiquetas):
                pred = self.predecir(x)
                error = y - pred
                # Actualiza los pesos y el sesgo
                self.pesos += self.learning_rate * error * x
                self.sesgo += self.learning_rate * error

# Datos de entrenamiento (Ingreso, Edad, Historial de Crédito, Monto Préstamo)
entradas = np.array([
    [5000, 30, 8, 15000],  # Aprobado
    [4000, 25, 6, 10000],  # Rechazado
    [6000, 40, 9, 20000],  # Aprobado
    [3500, 35, 5, 12000],  # Rechazado
    [7000, 45, 10, 30000], # Aprobado
])

# Etiquetas (1 = Aprobado, 0 = Rechazado)
etiquetas = np.array([1, 0, 1, 0, 1])

# Crear y entrenar el perceptrón
perceptron = Perceptron(input_size=4)  # 4 características de entrada
perceptron.entrenar(entradas, etiquetas, epochs=10)

# Probar el perceptrón después de entrenar con nuevos clientes
print("Predicciones:")
nuevos_clientes = np.array([
    [5500, 32, 7, 16000],  # Cliente con ingresos medios, edad media, historial bueno
    [3000, 28, 4, 11000],  # Cliente con ingresos bajos, historial regular
    [8000, 50, 10, 25000], # Cliente con altos ingresos y excelente historial
])

for cliente in nuevos_clientes:
    prediccion = perceptron.predecir(cliente)
    print(f"Cliente: {cliente} -> Predicción: {'Aprobado' if prediccion == 1 else 'Rechazado'}")
