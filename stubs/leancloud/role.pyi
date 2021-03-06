from typing import Dict

import leancloud
from leancloud.acl import ACL
from leancloud.relation import Relation


class Role(object):
    def __init__(self, name: str=None, acl: ACL=None) -> None:...

    def get_name(self) -> str:...

    def set_name(self) -> Role:...

    def get_users(self) -> Relation:...

    def get_roles(self) -> Relation:...

    def validate(self, attrs: Dict) -> bool:...
