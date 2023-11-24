# Installation instructions

Python Install:

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```
Clonamos el repositorio:
```bash
sudo apt install git
git clone https://github.com/ccjuantrujillo/melanoma-analysis.git
```

Create virtual environment:

```bash
sudo apt install python3.10-venv
sudo python3 -m venv ./venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install Flask
pip install python-dotenv
pip install Flask-CORS

```

Run the application:

```bash
python3 app.py
```

