import pandas as pd
import matplotlib.pyplot as plt
import os

# Usamos parse_dates para que pandas interprete la columna como fecha real
# y no como texto, lo que permite operaciones temporales como agrupar por mes
df = pd.read_csv('datos/ventas.csv', parse_dates=['sales_date'])

# Indicador 1: Ventas totales
# sum() sobre todos los registros nos da el volumen total del negocio
# lo que permite evaluar si el año fue positivo o negativo globalmente
ventas_totales = df['sales_amount'].sum()
print(f'Ventas totales: ${ventas_totales:,.2f}')

# Indicador 2: Promedio diario
# mean() es más útil que la suma para comparar períodos de distinta duración
# ya que normaliza el volumen de ventas por cantidad de días
promedio_diario = df['sales_amount'].mean()
print(f'Promedio diario: ${promedio_diario:,.2f}')

# Indicador 3: Día con mayor venta
# idxmax() devuelve el índice de la fila con el valor más alto
# luego lo usamos para recuperar la fecha correspondiente a ese pico
dia_max = df.loc[df['sales_amount'].idxmax(), 'sales_date']
monto_max = df['sales_amount'].max()
print(f'Mejor dia de ventas: {dia_max.date()} con ${monto_max:,.2f}')

# Indicador 4: Ventas por mes
# Convertimos la fecha a período mensual para agrupar todos los días
# de un mismo mes en un solo registro y ver tendencias estacionales
df['mes'] = df['sales_date'].dt.to_period('M')
ventas_mensuales = df.groupby('mes')['sales_amount'].sum()
print(f'\nVentas por mes:\n{ventas_mensuales}')

# Gráfico de barras porque permite comparar visualmente el volumen
# entre meses de forma clara, a diferencia de una línea que sugiere continuidad
ventas_mensuales.plot(kind='bar', figsize=(10,5), color='steelblue')
plt.title('Evolucion de Ventas por Mes - 2024')
plt.xlabel('Mes')
plt.ylabel('Monto ($)')
plt.tight_layout()

# Guardamos en /resultados para respetar la estructura del repositorio
# exist_ok=True evita errores si la carpeta ya existe
os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/grafico_ventas.png', dpi=150)
print('\nGrafico guardado en /resultados/')
