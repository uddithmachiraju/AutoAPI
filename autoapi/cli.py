import argparse 
from autoapi.main import run_server

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

    args = parser.parse_args() 

    if args.command == "run":
        run_server(args.config) 

if __name__ == "__main__":
    main()