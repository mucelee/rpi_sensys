# Get the base image
FROM  python:2.7-slim

# Set working directory
WORKDIR /san_example/

# Copy source files
ADD . /san_example/

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install any needed packages specified in requirements.txt
#RUN pip install -i https://pypi.python.org/simple -U pip distribute
#RUN pip install -r requirements.txt

# Run the application
CMD ["python" ,"exampleSAN.py"]
