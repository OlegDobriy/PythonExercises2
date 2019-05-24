from fixture.application import Application
import pytest
import json
import os.path
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'

    def __init__(self, config='target.json', browser='chrome'):
        self.browser = browser
        path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', config)
        with open(path_to_config_file) as config_file:
            self.target = json.load(config_file)

    def init_fixtures(self):
        self.fixture = Application(browser=self.browser, base_url=self.target['web']['baseUrl'])
        self.fixture.session.check_login(username=self.target['web']['username'], password=self.target['web']['password'])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def create_group(self, group):
        self.fixture.group.create(group)

    def get_group_list(self):
        return self.dbfixture.get_groups_list()

    def group_lists_should_be_equal(self, old_list, new_groups_list):
        assert sorted(old_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list, key=Group.sorting_id_or_maxsize)



