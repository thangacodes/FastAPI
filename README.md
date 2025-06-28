# FastAPI

## What is FastAPI?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It’s designed to be easy to use and to help you build robust APIs quickly.

In this project, I created a script called `macapp.py` that demonstrates how to build a simple FastAPI application.

---

### How to Create and Test a FastAPI API Locally

# Step 1: Install Required Packages

Before you start, you need to install the necessary Python packages: `fastapi` and `uvicorn`.

Run the following command to install these packages:

pip install fastapi uvicorn

# Step 2: Verify Installation
To confirm that the packages were installed correctly, you can run the following commands:

pip show fastapi

pip show uvicorn

Or you can check the installed packages list filtered by name:

pip list | grep fastapi

pip list | grep uvicorn

# Running FastAPI Application:
Once you have macapp.py ready, you can run your FastAPI app locally with uvicorn:

uvicorn macapp:app --reload

If you are running a FastAPI application with Uvicorn on an EC2 instance using a public IP address, you should run the command as follows:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Here, macapp is the filename (without .py), and app is the FastAPI instance inside that file.

The --reload flag enables auto-reload on code changes, which is useful during development.

## Next Steps:
Open your browser and navigate to the page to see your API in action.

http://127.0.0.1:8000/ 

http://127.0.0.1:8000/root_page

http://127.0.0.1:8000/ansv

http://127.0.0.1:8000/pkv

http://127.0.0.1:8000/pyv

http://127.0.0.1:8000/tfv

