from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Presentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 30px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
        }
        table {
            width: 70%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #333;
            padding: 12px;
            text-align: center;
        }
        th {
            background-color: #34495e;
            color: white;
        }
        td {
            background-color: #ecf0f1;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Presentation</h1>
    <p>The TCP/IP model is the foundation of communication over the Internet. 
    It consists of layers that work together to enable data transmission between computers.</p>
    
    <h2>TCP/IP Layers</h2>
    <table>
        <tr>
            <th>Layer</th>
            <th>Protocol Examples</th>
            <th>Functions</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, FTP, SMTP, DNS</td>
            <td>User interaction, data presentation</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
            <td>Reliable delivery, segmentation, error detection</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IP, ICMP</td>
            <td>Logical addressing, routing packets</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, Wi-Fi</td>
            <td>Physical transmission of data</td>
        </tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()