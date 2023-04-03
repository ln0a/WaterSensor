### Raspberry Pi setup:

`sudo apt update && sudo apt upgrade`

`sudo apt install python3-dev python3-pip python3-vlc vlc`

`sudo pip3 install spidev`

`sudo pip3 install mfrc522`

Enable SPI Interface in `raspi-config`

`sudo reboot`


### RFID reader setup:

Connect RFID reader to Raspberry Pi IO pins according to [this guide](https://pimylifeup.com/raspberry-pi-rfid-rc522/).

![RFID connection](https://cdn-images-1.medium.com/v2/resize:fit:1600/1*V7jGDYS_9IL1r24QZyzj6g.jpeg)

Run the read / write test with:
`python3 src/setup_test/write.py` and `python3 src/setup_test/read.py`


## NeoPixel Ring Setup

Follow [this guide](https://cdn-learn.adafruit.com/downloads/pdf/neopixels-on-raspberry-pi.pdf) to install custom libraries for NeoPixel on Rasperry Pi.