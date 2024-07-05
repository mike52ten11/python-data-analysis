def call_weather_api():
    import requests

    endpoint = "http://10.52.165.42/backend/api/v1/obs/cb_grid_lastest/"
    params = {"latlon": "23,121"}
    auth_token = "54dd375c9dea42298bc7905e5de24590"

    try:
    # 向資源發送請求，並傳遞該資源所需參數
    response = requests.get(endpoint, params=params, headers={"Authorization": f"Token {auth_token}"})

    # 請求成功回傳資料
    if response.status_code == 200:
        #result = response.json()
        print(f"success! data= {result}")

    else:
        # 請求失敗的status_code
        print(f"Error: {response.status_code} {response}")

    except Exception as e:
    print(f"An error occurred: {str(e)}")

def call_llm_api():
    import requests

    LLAMA_FACTORY_API_URL = "http://10.52.121.112:30224/v1/chat/completions"
    LLAMA_FACTORY_API_KEY = " "  # 請將your-api-key替換為您的實際API金鑰 
    prompt = "批量讀取csv並畫合鬚圖且保存畫圖的數據"

    headers = {
        "Authorization": f"Bearer {LLAMA_FACTORY_API_KEY}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "model": "string",  # 替換為您的模型名稱
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # 向LLaMA-Factory API發送POST請求
    response =  requests.post(LLAMA_FACTORY_API_URL, json=data, headers=headers)
    # response = requests.post(url, params=params)

    if response.status_code == 200:
        # 如果成功,处理响应的数据
        data = response.json()    
        reaponse_message = data["choices"][0]["message"]
        print(f'{reaponse_message["role"]}:\n{reaponse_message["content"]}')    
    else:
        print("Request failed:", response.status_code)
        print(data)  


# call_llm_api()

call_weather_api()