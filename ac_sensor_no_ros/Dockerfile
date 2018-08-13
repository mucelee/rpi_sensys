# Get the base image
FROM hypriot/rpi-python

# Set the working directory
WORKDIR /ac_sensor/

# Install prerequisites for ADC library (SoC bcm2835)
RUN /bin/bash -c "apt-get update && apt-get install -y automake libtool build-essential python-dev wget git"
RUN /bin/bash -c "wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.45.tar.gz && \
                  tar zxvf bcm2835-1.45.tar.gz"
RUN /bin/bash -c "ls && cd bcm2835-1.45 && ls && \
                  #autoreconf -vfi && \
		  ./configure && \
                  make CXXFLAGS=-fPIC CFLAGS=-fPIC && make install"
### We are skipping the "make check" step due to not having access to /dev/mem/ in build environment

# Install ADC library (py-ads1256)
RUN /bin/bash -c "cd ~ && git clone https://github.com/fabiovix/py-ads1256.git && \
		  cd py-ads1256 && \
		  python setup.py install"

# Copy files to workspace
ADD . /ac_sensor

# Launch the ros package
CMD ["python", "ac_sensor.py"]
