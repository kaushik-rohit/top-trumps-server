from app import app

if __name__ == "__main__":
    host_addr = '0.0.0.0'
    app.run(host= host_addr, port=5001, debug=True)