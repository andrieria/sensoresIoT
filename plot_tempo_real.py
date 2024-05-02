import serial
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arquivo = "dados_sensor.csv"
leitura_temperatura = []
leitura_humidade = []
ser = serial.Serial('COM12', 9600) # abre porta serial COM6 

fig, (ax1, ax2) = plt.subplots(2)
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Temperatura (°C)')
ax1.set_xlim([0, 50])
ax1.set_ylim([0, 40])

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Humidade (%)')
ax2.set_xlim([0, 50])
ax2.set_ylim([0, 100])

def update(frame):
    while ser.inWaiting() == 0:
        pass

    dados = str(ser.readline().decode("utf-8"))
    print(dados)
    sep = dados.split(";")
    temperatura = float(sep[0])
    humidade = float(sep[1])

    with open(arquivo, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Temperatura', 'Umidade'])
        csv_writer.writerow([temperatura, humidade])

    leitura_temperatura.append(temperatura)
    leitura_humidade.append(humidade)

    ax1.clear()
    ax2.clear()

    ax1.plot(leitura_temperatura, color='blue')
    ax2.plot(leitura_humidade, color='green')

    ax1.set_xlabel('Tempo (s)')
    ax1.set_ylabel('Temperatura (°C)')
    ax1.set_xlim([max(0, len(leitura_temperatura) - 50), len(leitura_temperatura)])
    ax1.set_ylim([0, 40])

    ax2.set_xlabel('Tempo (s)')
    ax2.set_ylabel('Humidade (%)')
    ax2.set_xlim([max(0, len(leitura_humidade) - 50), len(leitura_humidade)])
    ax2.set_ylim([0, 100])

ani = FuncAnimation(fig, update, interval=100)

plt.show()
