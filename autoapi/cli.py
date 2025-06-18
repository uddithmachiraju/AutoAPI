import argparse 
from autoapi.main import run_server
from autoapi.docker_utils import dockerize_app

def main():
    parser = argparse.ArgumentParser(
        prog = "autoapi",
        description = "AutoAPI CLI - Instantly turn config into REST API")
    
    subparser = parser.add_subparsers(dest = "command", help = "Available commands")

    run_parser = subparser.add_parser("run", help = "Run the AutoAPI server") 
    run_parser.add_argument(
        "--config",
        type = str, 
        default = "config.yaml" ,
        help = "Path to YAML file" 
    )

    docker_parser = subparser.add_parser("dockerize", help = "Build and run the application using Docker") 
    docker_parser.add_argument(
        "--dockerfile",
        type = str, 
        default = "Dockerfile",
        help = "Path to the Dockerfile (default: Dockerfile)"        
    )

    args = parser.parse_args() 

    if args.command == "run":
        run_server(args.config) 

    if args.command == "dockerize":
        dockerize_app(args.dockerfile)  

if __name__ == "__main__":
    main()