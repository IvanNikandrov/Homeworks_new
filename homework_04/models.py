from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text
)

PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost:5434/blog"
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
    posts = relationship('posts', back_populates='users')

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
    users = relationship('users', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}'

    def __repr__(self):
        return str(self)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def save_user_in_db(data):
    async with async_session() as session:
        async with session.begin():
            for user in data:
                session.add(User(
                    name=user['name'],
                    username=user['username'],
                    email=user['email']
                ))

async def save_post_in_db(data):
    async with async_session() as session:
        async with session.begin():
            for post in data:
                session.add(Post(
                    user_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                ))


