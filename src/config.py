import os
from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema


@dataclass
class Organization:
    name: str


@dataclass
class User:
    username: str
    password: str
    organization: str


@dataclass
class Config:
    ALLOWED_HOSTS: list
    SECRET_KEY: str
    DEBUG: bool
    SWAGGER_TITLE: str
    SWAGGER_DESCRIPTION: str
    KNOX_TOKEN_TTL_DAYS: int

    # Fixtures instead of CRUD
    ORGANIZATIONS: list[Organization]
    USERS: list[User]


config_path = "/../config.yaml"

with open(os.path.dirname(__file__) + config_path) as f:
    config_data = yaml.safe_load(f)

config: Config = class_schema(Config)().load(config_data)
