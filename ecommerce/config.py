from os import getenv

APP_ENV = getenv('APP_ENV', 'development')
DATABASE_USERNAME = getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', '123')
DATABASE_HOST = getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = getenv('DATABASE_NAME', 'ecommerce')
TEST_DATABASE_NAME = getenv('TEST_DATABASE_NAME', 'ecommerce_test')
