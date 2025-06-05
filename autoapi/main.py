import os 
import yaml 
import importlib
from flask import Flask, jsonify, request

def response_handler(response_config, method, url_params):
    if response_config["type"] == "raw":
        return jsonify(
            {
                "message" : response_config["value"]
            }
        )
    elif response_config["type"] == "python":
        module = importlib.import_module(response_config["value"]) 
        func = getattr(module, response_config["function"]) 

        input_data = {}
        if request.method in ("POST", "PUT"):
            input_data = request.get_json()
        elif request.method == "DELETE":
            result = func(url_params or {})
            return jsonify(result) 

        result = func(input_data, url_params or {}) 
        return jsonify(result) 

def run_server(config_path = "config.yaml"):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}") 
    
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file) 

    app = Flask(__name__) 

    environment = data['environment']
    config = data[environment]["flask"]
    endpoints = data[environment]["endpoints"] 

    for endpoint in endpoints:
        path = endpoint["path"]
        method = endpoint["method"]
        response = endpoint["response"]

        def handler(response_config = response, method = method, **kwargs):
            return response_handler(response_config, method, url_params = kwargs) 

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
