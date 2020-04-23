from app import app

if __name__ == "__main__":
    host_addr = 'localhost'
    app.run(host= host_addr, port=5001, debug=True)