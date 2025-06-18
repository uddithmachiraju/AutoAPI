import re 
import subprocess 

def extract_port(dockerfile):
    with open(dockerfile, "r") as file:
        content = file.read() 

    match = re.search(r'EXPOSE\s+(\d+)', content)
    if match:
        return match.group(1)
    else:
        return "No port was exposed!"

def dockerize_app(dockerfile):
    image_name = "autoapi-image"
    container_name = "autoapi-container"

    port = extract_port(dockerfile) 

    subprocess.run(
        [
            "docker", "build", "-f", dockerfile, "-t", image_name, "."
        ], check = True
    )

    subprocess.run(
        [
            "docker", "run", "-d", "--name", container_name, "-p", f"{port}:{port}", image_name
        ], check = True
    )