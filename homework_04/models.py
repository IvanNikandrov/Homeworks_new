from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text
)
import os

# PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost:5434/blog"
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost:5434/blog"
PG_ECHO = True

engine = create_async_engine(PG_CONN_URI, echo=PG_ECHO)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False, default='', server_default='')
    username = Column(String(20), nullable=False, default='', server_default='')
    email = Column(String(), nullable=False, default='', server_default='')
    posts = relationship('Post', back_populates='users')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name={self.name}, ' \
               f'username={self.username}, email={self.email})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False, default='', server_default='')
    body = Column(Text(), nullable=False, default='', server_default='')
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    users = relationship('User', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}'

    def __repr__(self):
        return str(self)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def save_user_and_post_in_db(user_data, post_data):
    async with async_session() as session:
        async with session.begin():
            for user in user_data:
                session.add(User(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email']
                ))
            for post in post_data:
                session.add(Post(
                    id=post['id'],
                    user_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                ))
