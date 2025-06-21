# AutoAPI | [GitHub](https://github.com/uddithmachiraju/AutoAPI)

> **No more boring and hardcoding of API for your model/application.**

- With AutoAPI, you don’t have to hardcode the endpoints you can simply define them in the `config.yaml` file, run the application, and boom! your API is up and running.

### Things that are added in this project:

1. We can include a environment that we need our application to be deployed in.
    
    ```yaml
    environment: dev # May be anything prod/staging
    
    dev: # Use the required env here
      parameters here:
        ....
    ```
    
2. We can select a framework(as of now only `Flask` was integrated).
    
    ```yaml
    flask:
      host: "0.0.0.0"
      port: 5000
      debug: true
    ```
    
3. As of now I included adding Endpoints in the `config.yaml` file with supported nested endpoints.
4. Two types of responses were added at this point.
    - `raw` - Some random text you want to appear or may be html for the frontend. In this case the `value`  may be anything in strings or a html file.
    - `python` - Execute a python function. Need to specify two things.
        1. `value` - Source of the python file
        2. `function` - Function we need to call when triggered.
    
    ```yaml
    endpoints:
      - path: "/books"
          routes: 
            - path: "/" 
              method: ["GET"]
              response: 
                type: "raw"
                value: "Welocome to AutoAPI"
    
            - path: "/add"
              method: ["POST"]
              response: 
                type: "python"
                value: "tests.book_api"
                function: "post_book"
    ```
4. **Added logging system** - Things you need to specify for adding logging
    - You can the logger from `autoapi.logger.get_logger`  function to add into your code.
    
    ```yaml
      logging:
        enabled: true     # false by default
        logfile: "access" # Name of the file
        level: "INFO"     # Type of log
    ```
    
5. **Added reload of YAML -** Reload of application when new things are added without any interruption.
    - `debounce_seconds` - reload at every `debounce_seconds`
    
    ```yaml
      reload:
        enabled: true         # false by default
        debounce_seconds: 2   # reload time(sec)
    ```
6. **Added Containerization -** Now we can containerize our application in one setup. 
    - This will automatically extract the port and other stuff (can be done later).
    - Will try to give it an another `yaml` file for docker and setup the things without any use of the `Dockerfile` from the user.
    - Need to return some output after containerizing the application.
    
    ```
     autoapi dockerize --dockerfile=Dockerfile # Source file
    ```

Currently, I’m still working on it, so it might take some time before the project is ready for cloud deployment. For now, I’m focusing on local deployment.