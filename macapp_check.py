from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
import subprocess

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def root_page():
    html_content = """
    <body style="background-color: skyblue;">
    <br></br>
    <h1>FastAPI:</h1>
      <h2>Select an option:</h2>
      <ul>
        <li><a href="/root_page" target="_blank">root_page</a></li>
        <li><a href="/pyv" target="_blank">pyv</a></li>
        <li><a href="/pkv" target="_blank">pkv</a></li>
        <li><a href="/tfv" target="_blank">tfv</a></li>
      </ul>
      <br></br>
      <h3> made with interest and love ❤️ by Thangacodes..</h3>
    </body>
    """
    return html_content

@app.get("/root_page", response_class=PlainTextResponse)
def root_text():
    print("Landing into the root page")
    try:
        banner = "Welcome to the FastAPI world.."
        return banner
    except Exception as error:
        return f"Error: {str(error)}"

@app.get("/tfv", response_class=PlainTextResponse)
def get_tf_version():
    print("Checking terraform version")
    try:
        result = subprocess.run(["terraform", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        return f"Error getting terraform version:\n{str(error)}"

@app.get("/pyv", response_class=PlainTextResponse)
def get_py_version():
    print("Checking python version")
    try:
        result = subprocess.run(["python", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        return f"Error getting python version:\n{str(error)}"

@app.get("/pkv", response_class=PlainTextResponse)
def get_pkr_version():
    print("Checking packer version")
    try:
        result = subprocess.run(["packer", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        return f"Error getting packer version:\n{str(error)}"
