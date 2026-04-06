from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD Pipeline is working successfully!"

if __name__ == '__main__':
    print("Starting Flask App...")   # <-- log add
    app.run(host='0.0.0.0', port=5000)