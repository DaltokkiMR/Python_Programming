import requests
import pprint

def get_rest_api_data():
    try:
        url = "https://rest-api-test-self.vercel.app/api/4"
        response = requests.get(url=url, timeout=10)

        if response.status_code != 200:
            print(f"요청 실패: status code: {response.status_code}")

        data = response.json()
        data = data['posts']
        return data
        

    except requests.exceptions.Timeout as e:
        print(f"서버 응답시간 초과: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

# processed_data = [[data['id'], data['title'], data['author']['name'], data['tags'][0], data['stats']['likes']] for data in get_rest_api_data()]
# print(processed_data)