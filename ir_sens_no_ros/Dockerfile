# Get the base image
#FROM resin/rpi-raspbian
FROM  hypriot/rpi-python

# Set working directory
WORKDIR /ir_sens/

# Copy source files
ADD . /ir_sens/

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    --no-install-recommends && \
rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install -i https://pypi.python.org/simple -U pip distribute
RUN pip install -r requirements.txt

# Run the application
CMD ["python" ,"ir.py"]
