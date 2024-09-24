import pandas as pd
import matplotlib.pyplot as plt

class ForecastingApp:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Fecha', 'Valor'])
    
    def add_data(self, fecha, valor):
        new_data = pd.DataFrame({'Fecha': [fecha], 'Valor': [valor]})
        self.data = pd.concat([self.data, new_data], ignore_index=True)
    
    def remove_data(self, fecha):
        self.data = self.data[self.data['Fecha'] != fecha]
    
    def edit_data(self, fecha, nuevo_valor):
        self.data.loc[self.data['Fecha'] == fecha, 'Valor'] = nuevo_valor

    def simple_moving_average(self, window):
        self.data['SMA'] = self.data['Valor'].rolling(window=window).mean()
    
    def plot_data(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Fecha'], self.data['Valor'], label='Datos Reales', marker='o')
        plt.plot(self.data['Fecha'], self.data['SMA'], label='Promedio Móvil', marker='x')
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title('Pronóstico Simple')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    app = ForecastingApp()
    
    # Agregar datos
    app.add_data('2024-01-01', 100)
    app.add_data('2024-01-02', 120)
    app.add_data('2024-01-03', 130)
    app.add_data('2024-01-04', 110)
    
    # Editar datos
    app.edit_data('2024-01-02', 125)
    
    # Eliminar datos
    app.remove_data('2024-01-03')
    
    # Calcular promedio móvil
    app.simple_moving_average(window=2)
    
    # Graficar
    app.plot_data()
