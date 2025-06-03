
import os 
import yaml 
from flask import Flask, jsonify 

def response_handler(response_config):
    if response_config["type"] == "raw":
        return jsonify(
            {
                "message" : response_config["value"]
            }
        )
    else:
        pass 

def run_server(config_path = "config.yaml"):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}") 
    
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file) 

    app = Flask(__name__) 

    environment = data['environment']           # Get the evironment details
    config = data[environment]["flask"]         # Get the flask config
    endpoints = data[environment]["endpoints"]  # Endpoints for the API

    for endpoint in endpoints:
        path = endpoint["path"]
        method = endpoint["method"]
        response = endpoint["response"]

        def handler(response_config = response):
            return response_handler(response_config) 

        app.add_url_rule(
            path, 
            endpoint = path,
            view_func = handler,
            methods = method
        )

    app.run(
        host = config["host"],
        port = config["port"],
        debug = config["debug"] 
    )
