"""empty message

Revision ID: 462e5f0b6353
Revises: 2bedf5e85f4b
Create Date: 2020-04-24 13:04:28.290024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462e5f0b6353'
down_revision = '2bedf5e85f4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Snow_Child',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False, comment='关联的公司用户id'),
    sa.Column('name', sa.String(length=20), nullable=True, comment='测试名字'),
    sa.PrimaryKeyConstraint('id'),
    comment='雪花算法子表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Snow_Child')
    # ### end Alembic commands ###
