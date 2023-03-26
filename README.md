# carbon-footprint
Python and Flask app to calculate individual carbon footprint on Docker

###Build the container image as per instructions on the Dockerfile
docker build -t carbon-app . 


####Run the carbon-app image created in step above
docker run -d -p 8000:5000 carbon-app


###Verify that the container is running
docker ps

###Verify on Chrome browser
http://localhost:8000

##Stop Docker container
docker stop <container ID>

##Delete all docker images
docker system prune -a 
