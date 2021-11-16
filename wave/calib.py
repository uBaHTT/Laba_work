import spidev #для работы с spi
import time 
import matplotlib.pyplot as plt #для отображения графика
import waveFunctions as wave #написанные функции


spi = spidev.SpiDev()
spi.open(0, 0) #открывваем нулеове устройства spi с нулевым чип селектом
spi.max_speed_hz = 1600000 #частота тактового сигнала

def getAdc(): #функция, возвращающая текущее значение ацп (вернёт 12и битное число, являющееся рез-ом отцифровки)
    adcResponse = spi.xfer2([0 , 0])   #для чтения ацп испольщуется такая функция (докуменатция)
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse [1]) >> 1

try:
    
    data = [] #массив измерений
    start = time.time()
    count = 0 #счетчик кол-ва измерений 

    while (time.time() - start < 10): #пока не прошло десять секунд в цикле записывается значение ацп и увеличивается счетчик кол-во опытов
        data.append(getAdc())
        count = count + 1
    
    wave.saveMeasures(data, count, 1, start, time.time()) #оформляем документы txt с измерениями отдельно написанной функцией 

    plt.plot(data)
    plt.show()
    

finally:
    spi.close()
  
