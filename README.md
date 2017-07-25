# FAIR DATool for data assestment
Application implemented as microservice running on port 8081

Build the image using the following command

```bash
$ docker build -t badge:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -p 8081:8081 badge
```

The application will be accessible at http://localhost:8081. 
To run it on Apache web server please add in the httpd configuration file
```
<VirtualHost *:80>
    ProxyPass /badge http://0.0.0.0:8081
    ProxyPassReverse /badge http://0.0.0.0:8081
</VirtualHost>
```
Command line tool run:
```
python makeitfair/fairrun.py 'http://dx.doi.org/10.17632/crnmszmb8h.1'
```
will produce output with FAIR metrics
```
http://dx.doi.org/10.17632/crnmszmb8h.1
F 4.0
A 5.0
I 1.5
R 3.5
```
