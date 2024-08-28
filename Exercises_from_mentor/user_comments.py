from base_page import MockApi
class Users(MockApi):

    # 1 - получить всех юзеров женского пола
    def get_users_by_sex(self, sex: str):
        """
        Фильтр по полу
        :param sex: ввести пол male/female
        :return: возвращает список пользователей
        """
        result = self.get('users')
        return [user for user in result if user['sex'] == sex]

    # 2 - получить всех юзеров, имена которых содержат букву S
    def find_users_by_name(self, letters):
        result = []
        for user in self.get('users'):
            if letters in user['name'].lower():
                result.append(user)
        return result

    # 3 - получить всех пользователей с четными ID
    def get_users_by_step_id(self, num_id: int):
        users_even_id = self.get('users')
        return [user for user in users_even_id if int(user['id']) % num_id == 0]

    def filter_by_date(self, date):
        res = self.get('users')
        return [user for user in res if user['createdAt'] > date]

    def get_ids(self):
        result = [user['id'] for user in self.get('users')]
        return result

    def get_id(self, name, value):
        result = []
        for i in self.get('users'):
            if value in i[name]:
                result.append(i['id'])
        return result


class Comments(MockApi):
    def get_all_comments(self):
        return self.get('comments')

    def get_comments_by_userId(self, ids: set) -> list:
        """
        Метод получения комментов по id пользователей
        :param ids: это список id пользователей
        :return: возвращает список комментов пользователей
        """
        comments_by_id = []
        for id in ids:
            comment = self.get(f'users/{id}/comments')
            comments_by_id.append(comment)
        return comments_by_id
    def get_comment_by_commentId(self, id: int):
        """
        Метод получения комментов по id самого комментария
        :param id: это целое число
        :return: возвращает словарь
        """
        comment = self.get(f'/comments/{id}')
        return comment

    def post_comm(self, data):
        response = self.post('comments', data)
        return response


    def get_comm_step(self, step: int):
        res = self.get('comments')
        every_step_comms = [res[i] for i in range(0, len(res), step)]
        return every_step_comms

    def put_comm_step(self, step, comm):
        res = self.get_all_comments()
        for i in range(0, len(res), step):
            self.put(f"users/{res[i]['userId']}/comments/{res[i]['id']}", {"text": comm})

