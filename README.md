# rpi_sensys
Sensors for RPi

## ac_sensor
- connect hardware (description coming later)

- install Raspbian Stretch on Raspberry (tested on Pi 3+)
- install docker `curl -sSL https://get.docker.com | sh`
- clone the git repo ON THE RASPBERRY `git clone https://github.com/mucelee/rpi_sensys.git`
- navigate to ac_sensor directory `cd ac_sensor`
- build the docker container `docker build -t ac_sensor .`
- run the docker container `docker run --privileged ac_sensor`

#### Testing ac_sensor
- list running docker containers `docker ps`
- attach a shell to the running ac_sensor container `docker exec -it <CONTAINER_ID> bash`
- list ros topics `rostopic list`
- listen to ac sensor `rostopic echo /sen_4/ac_sensor`
