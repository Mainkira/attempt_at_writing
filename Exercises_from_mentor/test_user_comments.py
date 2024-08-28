from user_comments import Users, Comments

import pytest
import random
import string

class TestMockApi(Users, Comments):
    # def __init__(self):
    #     self.users = Users()
    #     self.comments = Comments()

    # 1 - получить всех юзеров женского пола
    # @pytest.mark.parametrize('sex', ["female", "male"])
    # def test_filter_by_sex(self, sex):
    #     users = self.users.get_users_by_sex(sex)
    #     assert all(user['sex'] == sex for user in users), "Имеются юзеры, не соответствующие фильтру sex"

    # 2 - получить всех юзеров, имена которых содержат букву S
    # @pytest.mark.parametrize("letters", ['S', 's'])
    # def test_users_with_s_in_name(self, letters):
    #     result = self.users.find_users_by_name(letters)
    #     for user in result:
    #         assert letters in user['name'].lower(), f'Юзер без {letters} в name'

    # 3 - получить всех пользователей с четными ID
    # @pytest.mark.parametrize('step', [step for step in range(1,5)])
    # def test_selection_by_step_id(self):
    #     result = self.users.get_users_by_step_id(2)
    #     print(result)
    #     for user in result:
    #         assert int(user['id']) % 2 == 0, "ID юзера не соответствует шагу"

    # 8 - найти всех пользователей, у которых поле createdAt больше чем 2024-06-19T14:50:55.890Z
    @pytest.mark.parametrize("dates", ['2024-06-19T14:50:55.890Z', '2024-06-20T14:50:55.890Z', '2024-06-21T22:50:55.890Z'])
    def test_users_regs_from_date(self, dates):
        result = self.users.filter_by_date(dates)
        print(result)
        for user in result:
            assert user['createdAt'] > dates, "Юзеры не отфлитровались по дате"


# 4 - получить все коменты для пользователей из задач 1-3
    def test_multiple_filters(self):
        selection = {user['id'] for user in self.get_users_by_sex("female") + self.find_users_by_name("s") + self.get_users_by_step_id(2)}
        print(selection)
        filtered_comments = self.get_comments_by_userId(selection)
        print(filtered_comments)
        for comms in filtered_comments:
            if 'Not found' not in comms:
                for comm in comms:
                    assert comm['userId'] in selection, "Имеются юзеры, не соответствующие фильтрам"

# 5 - добавить коммент для пользователя у которого имя Isaac
    @pytest.mark.parametrize("comments", ['I am Isaac', 'I am a lord of the world', 'I want to sleep'])
    def test_post_comms_for_users_by_name(self, comments):
        isaacs_ids = self.users.get_id('name', 'Isaac')
        for id in isaacs_ids:
            self.comments.post_comm({'text': comments, "userId": id})
        for comms in self.comments.get_all_comments():
            if comms['text'] == comments:
                assert comms['userId'] in isaacs_ids, "Коммент не у Исаака"
        # for i in self.comments.get_all_comments():
        #     if i['text'] == comments:
        #         self.delete('users/' + i['userId'] + '/comments/' + i['id'])
        # assert comments not in self.comments.get_all_comments()

    # 6 - получить каждый 3 коммент, отредактировать ему текст на TESTapiTEST
    @pytest.mark.parametrize('step', [random.randint(1,5)])
    @pytest.mark.parametrize('text', ['PKA1', 'PKA2', 'PKA3'])
    def test_change_every_step_comm(self, step, text):
        self.comments.put_comm_step(step, text)
        result = self.comments.get_all_comments()
        print(result)
        for comm in result:
            if result.index(comm) % step == 0:
                print(comm)
                assert comm['text'] == text, "Текст не отредактирован, ошибка в запросе put"



# 7 - получить случайное количество коментов из шага 6 и удалить их
    @pytest.mark.parametrize('step', [3, 4])
    def test_rip_random_comm(self, step):
        res = self.get_comm_step(3)
        print(res)
        quantity = random.randint(0, len(res)-1)
        for _ in range(quantity):
            index_for_remove = random.choice(range(len(res)))
            id = res[index_for_remove]['id']
            userId = res[index_for_remove]['userId']
            rip_comm = self.delete(f'users/{userId}/comments/{id}')
            print(rip_comm)
            assert 'Not found' in self.get_comment_by_commentId(id), "Комментарий не удален"







