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