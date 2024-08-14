from base_page import MockApi
class Users(MockApi):

    # 1 - получить всех юзеров женского пола
    def get_female_users(self):
        return self.get('/users?sex=female')

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

    def get_users_from_date(self, date):
        res = self.get('users')
        return [user for user in res if user['createdAt'] > date]

    def get_ids(self):
        result = [d['id'] for d in self.get('users')]
        return result

    def get_id(self, name, value):
        result = []
        for i in self.get_all_users():
            if value in i[name]:
                result.append(i['id'])
        return result


class Comments(MockApi):
    def get_all_comments(self):
        return self.get('comments')

    def get_some_comments(self, ids: set) -> list:
        """
        Метод получения комментов по id ползователей
        :param ids: это список id пользователей
        :return: возвращает список комментов пользователей
        """
        some_comments = []
        for id in ids:
            comment = self.get(f'users/{id}/comments')
            some_comments.append(comment)
        return some_comments

    def post_comm(self, data):
        response = self.post('comments', data)
        return response


    def get_comm_step(self, step):
        res = self.get('comments')
        every_step_comms = [res[i] for i in range(0, len(res), step)]
        return every_step_comms

    def put_comm_step(self, step, comm):
        res = self.get_all_comments()
        for i in range(0, len(res), step):
            change_comm = self.put(f"users/{res[i]['userId']}/comments/{res[i]['id']}", {"text": comm})
            print(change_comm)
        return

# 1 - получить всех юзеров женского пола
# female_users = Users().get_female_users()
#pprint.pprint(female_users)
# for dict in female_users:
    # assert dict['sex'] == 'female', 'SEX isn\'t female'

# # 2 - получить всех юзеров, имена которых содержат букву S
# find_s = Users().get_users_with_s()
# # pprint.pprint(find_s)


# # 3 - получить всех пользователей с четными ID
# filtered_users_by_id = Users().get_users_with_even_id()
# pprint.pprint(filtered_users_by_id)

# # # 4 - получить все коменты для пользователей из задач 1-3
# selection = {user['id'] for user in female_users + find_s + filtered_users_by_id}
# # print(sorted(selection))
# all = Comments().get_some_comments(selection)
# pprint.pprint(all)

# 5 - добавить коммент для пользователя у которого имя Isaac
# isaacs_ids = MockApi().get_id('name', 'Isaac')
# # print(isaacs_ids)
# new_comms = []
# for id in isaacs_ids:
#     r = Comments().post_comm({'text': 'WWW2', "userId": id})
#     print(r)
# # pprint.pprint(Comments().get_some_comments(isaacs_ids))
#
# # # # Удаление созданных комментов
# all_comms = Comments().get_all_comments()
# for i in all_comms:
#     if i['text'] == 'WWW2':
#         rip = MockApi().delete('users/' + i['userId'] + '/comments/' + i['id'])
#         # print(rip)
#
# # # 6 - получить каждый 3 коммент, отредактировать ему текст на TESTapiTEST
# every_third_comm = Comments().put_comm_step(3, "TESTapiTEST_PKA3")
# # pprint.pprint(every_third_comm)
#
#
# # # 7 - получить случайное количество коментов из шага 6 и удалить их
# rip_some_of_the_every_third_comm = Comments().get_comm_step(3)
# random_count = [random.randint(0, len(rip_some_of_the_every_third_comm)) for _ in range(3)]
# # print(random_count)
# # print(len(rip_some_of_the_every_third_comm))
# for i in random_count:
#     del rip_some_of_the_every_third_comm[i]
# # pprint.pprint(rip_some_of_the_every_third_comm)

# 8 - найти всех пользователей, у которых поле createdAt больше чем 2024-06-19T14:50:55.890Z
# users_from_some_date = Users().get_users_from_date('2024-06-19T14:50:55.890Z')
# # pprint.pprint(users_from_some_date)
# assert all(dict['createdAt'] > date for dict in users_from_some_date), "Имеются юзеры младше указанной даты"
