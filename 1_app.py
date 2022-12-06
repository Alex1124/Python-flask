from flask import Flask


'''The flask object implements a WSGI application and acts as the central object. It is passed the name of the module or package of the application. 
Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.

The name of the package is used to resolve resources from inside the package or the folder the module is contained in depending on if the package parameter resolves to an actual python package (a folder with an __init__.py file inside) or a standard module (just a .py file).

For more information about resource loading, see open_resource.

Usually you create a Flask instance in your main module or in the __init__.py file of your package like this:

from flask import Flask
app = Flask(__name__)
:param import_name: the name of the application package
:param static_url_path: can be used to specify a different path for the
                        static files on the web. Defaults to the name of the static_folder folder.
:param static_folder: The folder with static files that is served at
    static_url_path. Relative to the application root_path or an absolute path. Defaults to 'static'.
:param static_host: the host to use when adding the static route.
    Defaults to None. Required when using host_matching=True with a static_folder configured.
:param host_matching: set url_map.host_matching attribute.
    Defaults to False.
:param subdomain_matching: consider the subdomain relative to
    SERVER_NAME when matching routes. Defaults to False.
:param template_folder: the folder that contains the templates that should
                        be used by the application. Defaults to 'templates' folder in the root path of the application.
:param instance_path: An alternative instance path for the application.
                      By default the folder 'instance' next to the package or module is assumed to be the instance path.
:param instance_relative_config: if set to True relative filenames
                                 for loading the config are assumed to be relative to the instance path instead of the application root.
:param root_path: The path to the root of the application files.
    This should only be set manually when it can't be detected automatically, such as for namespace packages.'''
app = Flask(__name__)   #__name__ 顯示目前在哪個模組下執行

'''Decorate a view function to register it with the given URL rule and options. Calls add_url_rule, which has more details about the implementation.

See url-route-registrations.

The endpoint name for the route defaults to the name of the view function if the endpoint parameter isn't passed.

The methods parameter defaults to ["GET"]. HEAD and OPTIONS are added automatically.'''
@app.route('/') #裝飾品 如果進入到根目錄 -> func
def home():
    name = input('輸入你的名子=\n')
    return f'hello {name}'

@app.route('/test') #裝飾品 如果進入到test目錄 -> func
def test():
    num1= int(input('輸入數字= '))
    num2= int(input('輸入數字= '))
    return f'{num1} and {num2}2數相乘={num1 * num2}'


'''Runs the application on a local development server.

Do not use run() in a production setting. It is not intended to meet security and performance requirements for a production server. 
Instead, see /deploying/index for WSGI server recommendations.

If the debug flag is set the server will automatically reload for code changes and show a debugger in case an exception happened.

If you want to run the application in debug mode, but disable the code execution on the interactive debugger,
you can pass use_evalex=False as parameter. This will keep the debugger's traceback screen active, but disable code execution.

It is not recommended to use this function for development with automatic reloading as this is badly supported. 
Instead you should be using the flask command line script's run support.

:param host: the hostname to listen on. Set this to '0.0.0.0' to
    have the server available externally as well. Defaults to '127.0.0.1' or the host in the SERVER_NAME config variable if present.
:param port: the port of the webserver. Defaults to 5000 or the
    port defined in the SERVER_NAME config variable if present.
:param debug: if given, enable or disable debug mode. See
    debug.
:param load_dotenv: Load the nearest .env and .flaskenv
    files to set environment variables. Will also change the working directory to the directory containing the first file found.
:param options: the options to be forwarded to the underlying Werkzeug
    server. See werkzeug.serving.run_simple for more information.'''
    
if __name__ == "__main__":  #如果進入主程式
    app.run()   #app 伺服器啟動