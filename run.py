from app import create_app

app = create_app('config.development') # initial app with config
if __name__ == "__main__":
    app.run(host='0.0.0.0')
