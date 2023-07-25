import speedtest
#  pip install speedtest-cli


test = speedtest.Speedtest()

test.get_best_server()
donwload = test.download()
upload = test.upload()

print(f'Ping: {test.results.ping} ms')
print(f'Download Speed: {round(donwload  / 1000 / 1000, 1)} Mbit/s')
print(f'Upload Speed: {round(upload  / 1000 / 1000, 1)} Mbit/s')


# example output

# Ping: 14.697 ms
# Download Speed: 76.1 Mbit/s
# Upload Speed: 78.4 Mbit/s
