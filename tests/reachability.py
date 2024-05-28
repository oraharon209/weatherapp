import subprocess

def test_site_up():
    print("Running test_site_up...")
    output = subprocess.check_output("curl http://127.0.0.1:9090 --max-time 3", shell=True)
    print("Output:", output)
    assert "Failed" not in str(output)

def test_connection():
    print("Running test_connection...")
    output = subprocess.check_output("curl --include http://127.0.0.1:9090", shell=True)
    print("Output:", output)
    status_code = int(str(output).split(" ")[1])
    print("Status Code:", status_code)
    assert status_code in range(200, 400)
