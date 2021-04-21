import os

print('Building Container')
print(os.system('sudo docker build -t quickstart_image .'))

print('Running Container')
print(os.system('docker run -d --name App_Quickstart -p 6060:80 quickstart_image'))