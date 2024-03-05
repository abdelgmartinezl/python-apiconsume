import os
import requests
import json

base_url = "https://api.todoist.com/rest/v2"
api_token = os.environ.get('TODOIST_API_TOKEN')

cabeceras = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

def get_ejemplo():
    response = requests.get(f"{base_url}/tasks", headers=cabeceras)
    if response.status_code == 200:
        data = response.json()
        print("Ejemplo GET - Response:")
        json_bonito = json.dumps(data, indent=4)
        print(json_bonito)
    else:
        print("Ejemplo GET - Error:", response.status_code)

def post_ejemplo():
    nuevo_data = {
        "content": "Nueva Tarea",
        "due_string": "tomorrow",
        "due_lang": "en"
    }
    response = requests.post(f"{base_url}/tasks", headers=cabeceras, data=json.dumps(nuevo_data))
    if response.status_code == 200:
        data = response.json()
        print("Ejemplo Post - Respuesta:")
        json_bonito = json.dumps(data, indent=4)
        print(json_bonito)
    else:
        print("Ejemplo Post - Error:", response.status_code)

def main():
    get_ejemplo()
    post_ejemplo()

if __name__ == "__main__":
    main()



