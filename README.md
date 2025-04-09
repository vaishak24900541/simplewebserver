# EX01 Developing a Simple Webserver
## 212224040355
## Date:09.04.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<center><h1>TCP/IP PROTOCOLS</h1><br>
</center>
<h3>
1. Application Layer Protocols - HTTP,FTP,DNS<br>
2. Transport Layer Protocols - TCP/UDP<br>
3. Internet Layer Protocols - IPV4/IPV6<br>
4. Link Layer Protocols - MAC<br>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-04-09 144324.png>)

![alt text](<Screenshot 2025-04-09 152451.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
