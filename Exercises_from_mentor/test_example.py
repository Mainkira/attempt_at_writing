from user_comments import Users


class TestUsers(Users):
    def test_female_users(self):
        female_users = self.get_female_users()
        assert all(dict['sex'] == "female" for dict in female_users), "Имеются юзеры не female"

    def test_users_with_s_in_name(self):
        result = self.get_users_with_s()
        assert 's' in result['name'],

