from todo import settings_api_hub
from waitress import serve
import sys
import environ


env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

app = settings_api_hub(debug=env('DEBUG'))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        api_host = sys.argv[1]
    else:
        api_host = env('API_HOST')

    if env('SERVER_MODE') == 'DEVELOPMENT':
        app.run(host=api_host, port=env('API_PORT'),debug=env('DEBUG'))
    else:
        serve(app, host=api_host, port=env('API_PORT'),threads=1)