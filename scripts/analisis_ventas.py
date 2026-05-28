import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar el dataset desde la carpeta /datos
df = pd.read_csv('datos/ventas.csv', parse_dates=['sales_date'])

# Indicador 1: Ventas totales del período
ventas_totales = df['sales_amount'].sum()
print(f'Ventas totales: ${ventas_totales:,.2f}')

# Indicador 2: Venta promedio diaria
promedio_diario = df['sales_amount'].mean()
print(f'Promedio diario: ${promedio_diario:,.2f}')

# Indicador 3: Día con mayor venta
dia_max = df.loc[df['sales_amount'].idxmax(), 'sales_date']
monto_max = df['sales_amount'].max()
print(f'Mejor dia de ventas: {dia_max.date()} con ${monto_max:,.2f}')

# Indicador 4: Ventas por mes
df['mes'] = df['sales_date'].dt.to_period('M')
ventas_mensuales = df.groupby('mes')['sales_amount'].sum()
print(f'\nVentas por mes:\n{ventas_mensuales}')

# Gráfico de evolución de ventas mensuales
ventas_mensuales.plot(kind='bar', figsize=(10,5), color='steelblue')
plt.title('Evolucion de Ventas por Mes - 2024')
plt.xlabel('Mes')
plt.ylabel('Monto ($)')
plt.tight_layout()

# Guardar gráfico en /resultados
os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/grafico_ventas.png', dpi=150)
print('\nGrafico guardado en /resultados/')
