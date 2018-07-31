# rpi_sensys
Sensors for RPi

For development setup, clone this repo to ROS's /catkin_ws/src/ folder

## ac_sensor
- connect hardware (description coming later)

- install Raspbian Stretch on Raspberry (tested on Pi 3+)
- install docker `curl -sSL https://get.docker.com | sh`
- clone the git repo ON THE RASPBERRY `git clone https://github.com/mucelee/rpi_sensys.git`
- navigate to ac_sensor directory `cd ac_sensor`
- build the docker container `docker build -t ac_sensor .`
- edit and run FIWARE settings in ac_sensor_docker_start in repo root folder

#### Testing ac_sensor
- list running docker containers `docker ps`
- attach a shell to the running ac_sensor container `docker exec -it <CONTAINER_ID> bash`
- list ros topics `rostopic list`
- listen to ac sensor `rostopic echo /sen_4/ac_sensor`


## ir_sensor
- connect hardware (description coming later)

- install Raspbian Stretch on Raspberry (tested on Pi 3+)
- install docker `curl -sSL https://get.docker.com | sh`
- clone the git repo ON THE RASPBERRY `git clone https://github.com/mucelee/rpi_sensys.git`
- navigate to ir_sens_no_ros directory `cd ir_sens_no_ros`
- build the docker container `docker build -t ir_sensor .`
- edit and run FIWARE settings in ir_sensor_docker_start in repo root folder

#### Testing ac_sensor
- check from orion CB if the data is available
- Ctrl+C after running the container should not show errors and indicate the URL the data is sent to
