# python/api/otp.py
from http.server import BaseHTTPRequestHandler
import json
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # generate 6-digit OTP
        otp = random.randint(100000, 999999)

        body = json.dumps({"otp": otp})

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))
        return
