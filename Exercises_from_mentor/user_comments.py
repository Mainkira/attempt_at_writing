from base_page import MockApi
class Users(MockApi):

    # 1 - получить всех юзеров женского пола
    def get_users_by_sex(self, sex: str)  -> list:
        """
        Фильтр по полу
        :param sex: ввести пол male/female
        :return: возвращает полный список словарей с параметрами 'createdAt', 'name', 'sex', 'id'
        """
        result = self.get('users')
        return [user for user in result if user['sex'] == sex]

    # 2 - получить всех юзеров, имена которых содержат букву S
    def find_users_by_name(self, letters: str) -> list:
        """
        Поиск пользователей по имени
        :param letters: ввести начальные буквы имени
        :return: возвращает полный список словарей с параметрами 'createdAt', 'name', 'sex', 'id'
        """
        result = []
        for user in self.get('users'):
            if letters in user['name'].lower():
                result.append(user)
        return result

    # 3 - получить всех пользователей с четными ID
    def get_users_by_step_id(self, num_id: int) -> list:
        """
        Выборка пользователей из списка по шагу
        :param num_id: число шага, через каоторый будут выбраны юзеры
        :return: возвращает полный список словарей с параметрами 'createdAt', 'name', 'sex', 'id'
        """
        users_even_id = self.get('users')
        return [user for user in users_even_id if int(user['id']) % num_id == 0]

    def filter_by_date(self, date) -> list:
        """
        Выборка юзеров моложе даты регистрации
        :param date: дата в формате ISO, тип данных string, например '2024-06-19T14:50:55.890Z'
        :return: возвращает полный список словарей с параметрами 'createdAt', 'name', 'sex', 'id'
        """
        res = self.get('users')
        return [user for user in res if user['createdAt'] > date]

    def get_ids(self) -> list:
        """
        Получение только айдишников всех пользователей
        :return: возвращает список айдишников (int) юзеров
        """
        result = [user['id'] for user in self.get('users')]
        return result

    def get_id(self, name: str, value) -> list:
        """
        Получение списка айдишников из списка пользователей, имя которых соответвует введенному значению
        :param name: параметр в списке users, в котором будет искаться значение, м.б. 'createdAt', 'name', 'sex', 'id'
        :param value: значение параметра, по которому нужно отфильтровать список, тип данных для id: int, для остальных string
        :return:  возвращает список айдишников (int)  подошедших юзеров
        """
        result = []
        for i in self.get('users'):
            if value in i[name]:
                result.append(i['id'])
        return result


class Comments(MockApi):

    def get_all_comments(self):
        """

        :return: возвращает список словарей с параметрами
        """
        return self.get('comments')

    def get_comments_by_userId(self, ids: set) -> list:
        """
        Метод получения комментов по id пользователей
        :param ids: это список id пользователей
        :return: возвращает список словарей комментов пользователей с параметрами 'createdAt','text','user_id','id','userId'
        """
        comments_by_id = []
        for id in ids:
            comment = self.get(f'users/{id}/comments')
            comments_by_id.append(comment)
        return comments_by_id
    def get_comment_by_commentId(self, id: int) -> dict:
        """
        Метод получения комментов по id самого комментария
        :param id: это целое число
        :return: возвращает словарь одного коммента с параметрами 'createdAt','text','user_id','id','userId'
        """
        comment = self.get(f'/comments/{id}')
        return comment

    def post_comm(self, data):
        """
        Размещение комментария пользователя
        :param data: словарь с параметрами 'text', 'userId'
        :return:
        """
        response = self.post('comments', data)
        return response


    def get_comm_step(self, step: int) -> list:
        """
        Получение выборки списка комментариев по шагу
        :param step: шаг, целое число
        :return: список словарей комментов, отсортированный по указанному шагу, с параметрами 'createdAt','text','user_id','id','userId'
        """
        res = self.get('comments')
        every_step_comms = [res[i] for i in range(0, len(res), step)]
        return every_step_comms

    def put_comm_step(self, step: int, comm: str):
        """
        Изменение комментариев по шагу из всего списка комментариев
        :param step: шаг, целое число
        :param comm: текст комментария
        :return:
        """
        res = self.get_all_comments()
        for i in range(0, len(res), step):
            self.put(f"users/{res[i]['userId']}/comments/{res[i]['id']}", {"text": comm})

r = Comments().get_all_comments()
print(r)