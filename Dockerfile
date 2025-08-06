FROM python:3.10

# state the port it runs
EXPOSE 5000

# Go into folder within Dockerimg where we can put app.py
WORKDIR /app 

RUN pip install flask 

# This means copy everything into this directory (as L7 mv us into app)
COPY . . 

# What command should run when this image starts up as a container
# Allows external client to make a request
# NOTE always leave a space between CMD
CMD ["flask", "run", "--host", "0.0.0.0"]

# now run
    # docker build -t rest-apis-flask-python .

# When done we should see this image in our desktop
# When we run the image, press additional options, and do some port routing, say to 5005

# To run docker containers using command line:
    #docker run -p 5000:5005 rest-apis-flask-python
# 5000:5005 is an example of port forwarding and will store data locally on port 5005

