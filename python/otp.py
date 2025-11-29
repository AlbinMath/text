from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/otp", methods=["GET"])
def get_otp():
    otp = random.randint(100000, 999999)  # 6-digit OTP
    return jsonify({"otp": otp})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
