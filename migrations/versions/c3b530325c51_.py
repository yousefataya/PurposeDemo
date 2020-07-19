"""empty message

Revision ID: c3b530325c51
Revises: bb05c85d4f11
Create Date: 2020-02-06 21:26:38.103678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b530325c51'
down_revision = 'bb05c85d4f11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artical_history_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('articalName', sa.String(), nullable=False),
    sa.Column('writtenDate', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('autherCode', sa.String(), nullable=False),
    sa.Column('autherName', sa.String(), nullable=False),
    sa.Column('articalCode', sa.String(), nullable=False),
    sa.Column('isResereved', sa.String(), nullable=False),
    sa.Column('reserevedBy', sa.String(), nullable=False),
    sa.Column('publishDate', sa.DateTime(), nullable=False),
    sa.Column('publishingHouse', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('articalCode'),
    sa.UniqueConstraint('autherCode')
    )
    op.create_table('artical_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('articalName', sa.String(), nullable=False),
    sa.Column('writtenDate', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('autherCode', sa.String(), nullable=False),
    sa.Column('autherName', sa.String(), nullable=False),
    sa.Column('articalCode', sa.String(), nullable=False),
    sa.Column('isResereved', sa.String(), nullable=False),
    sa.Column('reserevedBy', sa.String(), nullable=False),
    sa.Column('publishDate', sa.DateTime(), nullable=False),
    sa.Column('publishingHouse', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('articalCode'),
    sa.UniqueConstraint('autherCode')
    )
    op.create_table('cron_job_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('jobName', sa.String(), nullable=False),
    sa.Column('JobCode', sa.String(), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('cronExpression', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('JobCode')
    )
    op.create_table('cron_job_lookup',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('lookupKey', sa.String(), nullable=False),
    sa.Column('lookupValue', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fetch_news_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('newsName', sa.String(), nullable=False),
    sa.Column('newsTitle', sa.String(), nullable=False),
    sa.Column('newsText', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('newsTitle')
    )
    op.create_table('history_news_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('newsName', sa.String(), nullable=False),
    sa.Column('newsTitle', sa.String(), nullable=False),
    sa.Column('newsText', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('newsTitle')
    )
    op.create_table('history_news_lookup',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('lookupKey', sa.String(), nullable=False),
    sa.Column('lookupValue', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('imageName', sa.String(), nullable=False),
    sa.Column('imageTitle', sa.String(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imageTitle')
    )
    op.create_table('keyword_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('keywork', sa.String(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_lookup',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('lookupKey', sa.String(), nullable=False),
    sa.Column('lookupValue', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subject_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('keywork', sa.String(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('keywork', sa.String(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('url_info',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(length=16), nullable=False),
    sa.Column('urlLink', sa.String(), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('isExpired', sa.Boolean(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('zip', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('url_info')
    op.drop_table('topic_info')
    op.drop_table('subject_info')
    op.drop_table('news_lookup')
    op.drop_table('keyword_info')
    op.drop_table('image_info')
    op.drop_table('history_news_lookup')
    op.drop_table('history_news_info')
    op.drop_table('fetch_news_info')
    op.drop_table('cron_job_lookup')
    op.drop_table('cron_job_info')
    op.drop_table('artical_info')
    op.drop_table('artical_history_info')
    # ### end Alembic commands ###
