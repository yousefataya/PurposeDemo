"""empty message

Revision ID: bb05c85d4f11
Revises: 256dbaafec5c
Create Date: 2020-02-06 17:00:10.751825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb05c85d4f11'
down_revision = '256dbaafec5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artical_info',
    sa.Column('id', sa.Integer(), nullable=False),
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
    op.drop_table('artical_info')
    # ### end Alembic commands ###
