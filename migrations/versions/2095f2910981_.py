"""empty message

Revision ID: 2095f2910981
Revises: 6018fa1854e8
Create Date: 2020-04-11 14:52:27.069005

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2095f2910981'
down_revision = '6018fa1854e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('myjob',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('creator', sa.BigInteger(), nullable=True, comment='创建人'),
    sa.Column('creatTime', sa.Integer(), nullable=True, comment='创建时间'),
    sa.Column('reviseTime', sa.Integer(), nullable=True, comment='更新时间'),
    sa.Column('reviser', sa.BigInteger(), nullable=True, comment='修改人'),
    sa.Column('isDel', sa.SmallInteger(), nullable=True, comment='是否删除 1-删除 0-未删除'),
    sa.Column('tittle', sa.String(length=50), nullable=True, comment='工作的标题'),
    sa.Column('reward', sa.String(length=20), nullable=True, comment='报酬'),
    sa.Column('place', sa.String(length=20), nullable=True, comment='地点'),
    sa.Column('settlement', sa.SmallInteger(), nullable=False, comment='工作结算方式 1-日结 2-周结 3-完工结'),
    sa.Column('isBagEating', sa.SmallInteger(), nullable=False, comment='是否包吃 1-是 2-否'),
    sa.Column('encase', sa.SmallInteger(), nullable=False, comment='是否包住 1-是 2-否'),
    sa.Column('isTrafficSubsidy', sa.SmallInteger(), nullable=False, comment='是否有交通补贴 1-是 2-否'),
    sa.Column('royalty', sa.SmallInteger(), nullable=False, comment='是否有提成 1-是 2-否'),
    sa.PrimaryKeyConstraint('id'),
    comment='300 工作表'
    )
    op.drop_table('job')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('creator', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True, comment='创建人'),
    sa.Column('creatTime', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='创建时间'),
    sa.Column('reviseTime', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='更新时间'),
    sa.Column('reviser', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True, comment='修改人'),
    sa.Column('isDel', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True, comment='是否删除 1-删除 0-未删除'),
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tittle', mysql.VARCHAR(length=50), nullable=True, comment='工作的标题'),
    sa.Column('reward', mysql.VARCHAR(length=20), nullable=True, comment='报酬'),
    sa.Column('place', mysql.VARCHAR(length=20), nullable=True, comment='地点'),
    sa.Column('settlement', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='工作结算方式 1-日结 2-周结 3-完工结'),
    sa.Column('isBagEating', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='是否包吃 1-是 2-否'),
    sa.Column('encase', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='是否包住 1-是 2-否'),
    sa.Column('isTrafficSubsidy', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='是否有交通补贴 1-是 2-否'),
    sa.Column('royalty', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='是否有提成 1-是 2-否'),
    sa.PrimaryKeyConstraint('id'),
    comment=' 工作表',
    mysql_comment=' 工作表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('myjob')
    # ### end Alembic commands ###
