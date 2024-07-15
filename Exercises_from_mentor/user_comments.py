import requests
import pprint
import random


class MockApi:
    url = 'https://66742d1675872d0e0a95683e.mockapi.io/api/v1/'

    def get(self, endpoint):
        response = requests.get(self.url + endpoint)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(self.url + endpoint, json=data)
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(self.url + endpoint, json=data)
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(self.url + endpoint)
        return response

    def get_all_users(self):
        users = self.get('users')
        return users

    def get_ids(self):
        result = [d['id'] for d in self.get('users')]
        return result

    def get_id(self, name, value):
        result = []
        for i in self.get_all_users():
            if value in i[name]:
                result.append(i['id'])
        return result


class Users(MockApi):

    # 1 - получить всех юзеров женского пола
    def get_female_users(self):
        female_users = self.get('/users?sex=female')
        return female_users

    # 2 - получить всех юзеров, имена которых содержат букву S
    def get_users_with_s(self):
        result = []
        for user in self.get('users'):
            if 's' in user['name'].lower():
                result.append(user)
        return result

    # 3 - получить всех пользователей с четными ID
    def get_users_with_even_id(self):
        users_even_id = self.get('users')
        return [user for user in users_even_id if int(user['id']) % 2 == 0]

    def get_users_from(self, date):
        res = self.get('users')
        return [c for c in res if c['createdAt'] > date]


class Comments(MockApi):
    def get_all_comments(self):
        all_commets = self.get('comments')
        return all_commets

    def get_some_comments(self, set_ids):
        some_comments = []
        for i in set_ids:
            comment = self.get(f'users/{i}/comments')
            some_comments.append(comment)
        return some_comments

    def post_comm(self, data):
        response = self.post('comments', data)
        return response

    def put_comm_step(self, step, comm):
        res = self.get('comments')
        for i in range(0, len(res), step):
            change_comm = self.put('users/' + res[i]['userId'] + '/comments/' + res[i]['id'], {"text": comm})
            print(change_comm)
        return

    def get_comm_step(self, step):
        res = self.get('comments')
        every_step_comms = [res[i] for i in range(0, len(res), step)]
        return every_step_comms


# 1 - получить всех юзеров женского пола
female_users = Users().get_female_users()
pprint.pprint(female_users)
#
# # 2 - получить всех юзеров, имена которых содержат букву S
find_s = Users().get_users_with_s()
pprint.pprint(find_s)
#
# # 3 - получить всех пользователей с четными ID
filtered_users_by_id = Users().get_users_with_even_id()
pprint.pprint(filtered_users_by_id)
#
# # 4 - получить все коменты для пользователей из задач 1-3
selection = {user['id'] for user in female_users + find_s + filtered_users_by_id}
# print(sorted(selection))
all = Comments().get_some_comments(selection)
pprint.pprint(all)

# 5 - добавить коммент для пользователя у которого имя Isaac
isaacs_ids = MockApi().get_id('name', 'Isaac')
print(isaacs_ids)
new_comms = []
for id in isaacs_ids:
    r = Comments().post_comm({'text': 'WWW2', "userId": id})
    print(r)
pprint.pprint(Comments().get_some_comments(isaacs_ids))
# #
# # # Удаление созданных комментов
all_comms = Comments().get_all_comments()
for i in all_comms:
    if i['text'] == 'WWW2':
        rip = MockApi().delete('users/' + i['userId'] + '/comments/' + i['id'])
        print(rip)
#
# # 6 - получить каждый 3 коммент, отредактировать ему текст на TESTapiTEST
every_third_comm = Comments().put_comm_step(3, "TESTapiTEST_PKA3")
pprint.pprint(every_third_comm)
#
#
# # 7 - получить случайное количество коментов из шага 6 и удалить их
rip_some_of_the_every_third_comm = Comments().get_comm_step(3)
random_count = random.randint(0, len(rip_some_of_the_every_third_comm))
# print(random_count)
# print(len(rip_some_of_the_every_third_comm))
for i in range(random_count):
    rip_some_of_the_every_third_comm.pop()
pprint.pprint(rip_some_of_the_every_third_comm)

# 8 - найти всех пользователей, у которых поле createdAt больше чем 2024-06-19T14:50:55.890Z
users_from_some_date = Users().get_users_from('2024-06-19T14:50:55.890Z')
pprint.pprint(users_from_some_date)
