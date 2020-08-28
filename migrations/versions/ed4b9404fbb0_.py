"""empty message

Revision ID: ed4b9404fbb0
Revises: 7001605c409a
Create Date: 2020-04-13 16:42:29.721404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed4b9404fbb0'
down_revision = '7001605c409a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('creator', sa.BigInteger(), nullable=True, comment='创建人'),
    sa.Column('creatTime', sa.Integer(), nullable=True, comment='创建时间'),
    sa.Column('reviseTime', sa.Integer(), nullable=True, comment='更新时间'),
    sa.Column('reviser', sa.BigInteger(), nullable=True, comment='修改人'),
    sa.Column('isDel', sa.SmallInteger(), nullable=True, comment='是否删除 1-删除 0-未删除'),
    sa.Column('message', sa.String(length=20), nullable=True, comment='搜索的信息'),
    sa.PrimaryKeyConstraint('id'),
    comment='303 热门搜索表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search')
    # ### end Alembic commands ###