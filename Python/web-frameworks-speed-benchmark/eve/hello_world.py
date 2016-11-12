from eve import Eve

app = Eve()

@app.route('/')
def hello_world():
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
