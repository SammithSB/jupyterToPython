# IPYNB to Python Converter

This is a Flask web application that converts Jupyter Notebook (.ipynb) files to Python (.py) scripts. The application allows users to upload a Jupyter Notebook file and download the corresponding Python script.

## Features

- Upload Jupyter Notebook (.ipynb) files.
- Convert the uploaded notebook to a Python (.py) script.
- Download the converted Python script.
- View and copy the converted Python script directly from the web interface.

## Technologies Used

- Python
- Flask
- nbformat
- nbconvert
- HTML/CSS (Bootstrap)

## Setup and Deployment

### Local Setup

1. **Clone the repository:**

    ```sh
    gh repo clone SammithSB/jupyterToPython
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**

    ```sh
    python app.py
    ```

5. **Access the application:**

    Open your browser and go to `http://127.0.0.1:5000`.


## Usage

1. **Upload your Jupyter Notebook:**
    - Click on the "Upload your Jupyter Notebook" button and select a `.ipynb` file from your computer.

2. **Convert the notebook:**
    - Click on the "Convert" button to convert the uploaded notebook to a Python script.

3. **View and download the Python script:**
    - The converted Python script will be displayed on the web page.
    - You can copy the code or download the script by clicking the "Download" button.

