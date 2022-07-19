from sqlalchemy import create_engine
import psycopg2


engine = psycopg2.connect(user="pavel", password="1111")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)




# 1111 это мой пароль для пользователя postgres
engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")
engine.connect()

