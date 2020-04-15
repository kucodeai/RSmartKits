## How to use

1. redirect to the repository \
   $ cd fan-control-script
2. open the .sh or .py file and modify the pwm value based on your preference and save \
   $ vi fan.sh 
3. execute it automatically when the machine is booted \
   $ sudo chmod +x fan.sh \
   $ sudo scp fan.sh /etc/init.d \
   $ sudo crontab -e \
   add  @reboot /etc/init.d/fan.sh  at the very top lane \
   $ sudo reboot
