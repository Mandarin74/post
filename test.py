from chekpost import get_post

id_check = 93512


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res


my_title = 'owbed'


def test_result(token):
    out = get_post(token)['data']
    result = []
    for items in out:
        result.append(items['title'])
    assert my_title in result
