import os
import subprocess
import time

WEATHERAPP_IP = os.getenv('WEATHERAPP_IP', '127.0.0.1')

def test_site_up():
    print("Running test_site_up...")
    try:
        output = subprocess.check_output(f"curl http://{WEATHERAPP_IP}:9090 --max-time 3", shell=True)
        print("Output:", output)
        assert "Failed" not in str(output)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect: {e}")
        raise

def test_connection():
    print("Running test_connection...")
    try:
        output = subprocess.check_output(f"curl --include http://{WEATHERAPP_IP}:9090", shell=True)
        print("Output:", output)
        status_code = int(str(output).split(" ")[1])
        print("Status Code:", status_code)
        assert status_code in range(200, 400)
    except subprocess.CalledProcessError as e:
        print(f"Connection error: {e}")
        raise

if __name__ == '__main__':
    time.sleep(5)  # Add a short sleep to ensure the service has time to start
    test_site_up()
    test_connection()
