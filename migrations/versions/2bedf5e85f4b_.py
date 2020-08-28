"""empty message

Revision ID: 2bedf5e85f4b
Revises: 18e24d87f8b7
Create Date: 2020-04-24 13:04:10.280359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2bedf5e85f4b'
down_revision = '18e24d87f8b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snow_child')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('snow_child',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False, comment='关联的公司用户id'),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True, comment='测试名字'),
    sa.PrimaryKeyConstraint('id'),
    comment='雪花算法子表',
    mysql_comment='雪花算法子表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
