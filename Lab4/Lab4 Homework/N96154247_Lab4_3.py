import serial
import time

# UART 設定
ser = serial.Serial(
    port="/dev/serial0",
    baudrate=9600,
    timeout=1
)


def send_data(data):
    if ser.is_open:
        ser.write((data + "\n").encode("utf-8"))
        print(f"已傳送：{data}")


def receive_data():
    if ser.is_open:
        incoming = ser.readline().decode("utf-8").strip()

        if incoming:
            print(f"收到資料：{incoming}")
            return incoming

    return None


try:
    print("UART 程式啟動，按 Ctrl+C 結束")

    send_value = 0

    while True:
        # 傳送數字
        send_data(str(send_value))

        # 接收並顯示資料
        receive_data()

        send_value += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("\n程式中斷")

finally:
    if ser.is_open:
        ser.close()

    print("串列埠已關閉")