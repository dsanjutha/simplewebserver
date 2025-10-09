from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
  <title>Device Specification</title>
</head>
<body>
  <h1 align="center">Device Specification (Sanjutha D)</h1>
  <table border="5" cellpadding="10" cellspacing="10">
    <tr>
      <th bgcolor="lightblue">S.No</th>
      <th bgcolor="lightblue">Device Specification</th>
      <th bgcolor="lightblue">Type</th>
    </tr>
    <tr>
      <td>1</td>
      <td>Device Name</td>
      <td>AEGX-001X</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Processor</td>
      <td>Octa-Core 2.5 GHz</td>
    </tr>
    <tr>
      <td>3</td>
      <td>RAM Capacity</td>
      <td>16 GB (15.8 GB usable)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Serial Number</td>
      <td>SN-98432-11223-XYZ</td>
    </tr>
    <tr>
      <td>5</td>
      <td>System Architecture</td>
      <td>64-bit Operating System</td>
    </tr>
  </table>
</body>
</html>

"""

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ("", 8000)
httpd = HTTPServer(server_address, myHandler)
print("My webserver is running...")
httpd.serve_forever()