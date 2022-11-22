import math
import speedtest

def byte_to_mb(size_byte):
    i = int(math.floor(math.log(size_byte, 1024)))
    power = math.pow(1024, i)
    size = round(size_byte/power, 2)

    return f"{size} Mbps"

wifi = speedtest.Speedtest()

print('Getting download speed...')
download_speed = wifi.download()

print('Getting upload speed...')
upload_speed = wifi.upload()

print(f"Download speed: {byte_to_mb(download_speed)} ")
print(f"Upload speed: {byte_to_mb(upload_speed)} ")