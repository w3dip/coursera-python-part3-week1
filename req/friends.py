import requests
import json
import time
import collections

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

def calc_age(uid):
    params = dict(user_ids = uid, v = 5.71, access_token = ACCESS_TOKEN)
    user = requests.get('https://api.vk.com/method/users.get', params)
    user_id = user.json()['response'][0]['id']

    params = dict(user_id = user_id, v = 5.71, access_token = ACCESS_TOKEN, fields = 'bdate')
    friends = requests.get('https://api.vk.com/method/friends.get', params)
    #print(json.dumps(json.loads(friends.content), indent=4, sort_keys=True))
    friends_ages = []
    for friend in friends.json()['response']['items']:
        birth_date_str = friend.get('bdate')
        if birth_date_str:
            try:
                birth_date = time.strptime(birth_date_str, "%d.%m.%Y")
                #print('Parsed date ' + time.strftime("%d.%m.%Y", birth_date))
                age = time.localtime().tm_year - birth_date.tm_year
                #print('Calculated age', age)
                friends_ages.append(age)
            except:
                pass
                #print('Can\'t parse date ' + birth_date_str)

    list.sort(friends_ages)
    sorted_ages = collections.Counter(friends_ages)
    #print(sorted_ages)
    return sorted_ages.most_common()


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
