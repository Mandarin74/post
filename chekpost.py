import requests
import yaml

go = requests.session()

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def get_login():
    path = data['path']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = data['path_2']
    get = requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()


def chreate(token):
    url = 'https://test-stand.gb.ru/api/posts'
    target = {'title': data['title'], 'description': data['description'], 'content': data['content']}
    new_post = requests.post(url=url, data=target, headers={'X-Auth-token': token})
    if new_post.status_code == 200:
        return new_post.json()



if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    print(chreate(token))