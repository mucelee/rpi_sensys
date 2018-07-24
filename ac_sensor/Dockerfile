# Get the base image
FROM esteve/ros:kinetic-robot-armhf

# Setup catkin workspace
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && \
                  mkdir -p /catkin_ws/src && \
                  cd /catkin_ws/src && \
                  catkin_init_workspace && \
                  cd /catkin_ws/ && \
                  catkin_make && \
                  echo 'source /catkin_ws/devel/setup.bash' >> ~/.bashrc"

#RUN /bin/bash -c "source ~/.bashrc"

# Install prerequisites for ADC library (SoC bcm2835)
RUN /bin/bash -c "apt-get update && apt-get install -y automake libtool build-essential python-dev wget"
RUN /bin/bash -c "wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.56.tar.gz && \
                  tar zxvf bcm2835-1.56.tar.gz"
RUN /bin/bash -c "cd bcm2835-1.56 && \
                  autoreconf -vfi && ./configure && \
                  make CXXFLAGS=-fPIC CFLAGS=-fPIC && make install"
### We are skipping the "make check" step due to not having access to /dev/mem/ in build environment

# Install ADC library (py-ads1256)
RUN /bin/bash -c "cd ~ && git clone https://github.com/fabiovix/py-ads1256.git && \
		  cd py-ads1256 && \
		  python setup.py install"

# Copy files to workspace
ADD . /catkin_ws/src/ac_sensor

# Build ROS package
#RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && \
#		  cd ~/catkin_ws/ && catkin_make"

# Launch the ros package
WORKDIR /catkin_ws/src/ac_sensor/
#CMD ["roslaunch", "ac_sensor", "ac_sensor.launch"]
CMD ["./run"]
