import subprocess
import datetime

# Get current execution time
exec_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {exec_time}")

# List of FastAPI URLs to check
urls = [
    "http://127.0.0.1:8000/pyv",
    "http://127.0.0.1:8000/tfv",
    "http://127.0.0.1:8000/pkv",
    "http://127.0.0.1:8000/av"
]

print("Starting health check of the web URLs...")

def hc(urls):
    for url in urls:
        print(f"\n Checking health for FastAPI Endpoints like: {url} \n")
        try:
            # Run curl command to get only the HTTP status code
            result = subprocess.run(
                ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
                capture_output=True,
                text=True,
                timeout=5
            )
            http_status = result.stdout.strip()

            # Evaluate the HTTP status code
            if http_status == "200":
                print(f"[{url}] app is healthy (HTTP {http_status})")
            else:
                print(f"[{url}] app is UNHEALTHY (HTTP {http_status})")

        except subprocess.TimeoutExpired:
            print(f"[{url}] Curl request timed out. Server might be down or unreachable.")
        except Exception as e:
            print(f"[{url}] Error during curl: {e}")

# Run health check 3 times
for i in range(3):
    print(f"\n --- Health Check Round {i+1} ---")
    hc(urls)
