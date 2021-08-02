from flask import Flask, jasonify, Response, request
app = Flask(__name__)

@app.route('', methods=['POST'])
def service-4(
