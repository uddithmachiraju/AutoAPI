import os 
import yaml 
import importlib
from autoapi.logger import get_logger
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
            result = func(input_data, url_params or {}) 
        elif request.method == "DELETE":
            result = func(url_params or {})
            return jsonify(result) 
        else: 
            result = func(url_params or {})

        return jsonify(result) 
    
def register_routes(app, base_path, route_definations):
    for endpoint in route_definations:
        raw_subpath = endpoint["path"]
        full_path = f"{base_path.rstrip('/')}/{raw_subpath.lstrip('/')}"

        # If there are nested routes in the endpoint
        if "routes" in endpoint:
            register_routes(app, full_path.rstrip("/"), endpoint["routes"]) 
        else:
            method = endpoint["method"]
            response = endpoint["response"]

            def handler(response_config = response, method = method, **kwargs):
                return response_handler(response_config, method, url_params = kwargs) 

            app.add_url_rule(
                full_path, 
                endpoint = full_path,
                view_func = handler,
                methods = method
            )

def run_server(config_path = "config.yaml"):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}") 
    
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file) 

    app = Flask(__name__) 

    environment = data['environment']
    config = data[environment]["flask"]
    endpoints = data[environment]["endpoints"] 
    logging_info = data.get(environment, {}).get("logging", {"enabled": "false"})

    logger = None 
    if logging_info.get("enabled", "false"):
        logger = get_logger(log_name = logging_info["logfile"], level = logging_info["level"])  

    register_routes(app, "", endpoints)

    app.logger = logger 

    if logger:
        @app.after_request
        def log_request(response):
            logger.info(f"{request.method} {request.path} {response.status_code}")
            return response

    app.run(
        host = config["host"],
        port = config["port"],
        debug = config["debug"] 
    )
