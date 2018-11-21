raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
sudo apt-get dist-update
sudo rpi-update
sudo reboot
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
sudo raspi-config
sudo apt-get upgrade
sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"
top
sudo apt-get install motion
sudo vi /etc/motion/motion.conf
sudo service motion restart
top
sudo vi /etc/motion/motion.conf
