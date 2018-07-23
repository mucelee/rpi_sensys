# Get the base image
FROM esteve/ros:kinetic-robot-armhf

# Setup catkin workspace
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && \
                  mkdir -p ~/catkin_ws/src && \
                  cd ~/catkin_ws/src && \
                  catkin_init_workspace && \
                  cd ~/catkin_ws/ && \
                  catkin_make && \
                  echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc"

RUN bin/bash -c "source ~/.bashrc"

# Install prerequisite for ADC library (SoC bcm2835)
RUN /bin/bash -c "apt-get install automake libtool && \
                  wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz && \
                  tar zxvf bcm2835-1.50.tar.gz && \
                  cd bcm2835-1.50 && \
                  autoreconf -vfi && \
                  ./configure && \
                  make && \
		  make check && \
		  make install"

# Install ADC library (py-ads1256)
RUN /bin/bash -c "apt-get install git build-essentials python-dev && \
		  cd ~ && \
		  git clone https://github.com/fabiovix/py-ads1256.git && \
		  cd py-ads1256 && \
		  python setup.py"

# Copy files to workspace
ADD . ~/catkin_ws/src/ac_sensor

# Build the ros package
CMD ["catkin_make"]

# Launch the ros package
CMD ["roslaunch", "ac_sensor", "ac_sensor.launch"]
