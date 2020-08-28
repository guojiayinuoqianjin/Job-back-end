"""empty message

Revision ID: 2065e835c502
Revises: b4993ef6a4e4
Create Date: 2020-04-14 20:51:01.223885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2065e835c502'
down_revision = 'b4993ef6a4e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('creator', sa.BigInteger(), nullable=True, comment='创建人'),
    sa.Column('creatTime', sa.Integer(), nullable=True, comment='创建时间'),
    sa.Column('reviseTime', sa.Integer(), nullable=True, comment='更新时间'),
    sa.Column('reviser', sa.BigInteger(), nullable=True, comment='修改人'),
    sa.Column('isDel', sa.SmallInteger(), nullable=True, comment='是否删除 1-删除 0-未删除'),
    sa.Column('name', sa.String(length=50), nullable=True, comment='用户的姓名'),
    sa.Column('age', sa.Integer(), nullable=True, comment='用户的年龄'),
    sa.Column('nativePlace', sa.String(length=50), nullable=True, comment='所在城市'),
    sa.Column('place', sa.String(length=50), nullable=True, comment='所在地级市'),
    sa.Column('phoneNumber', sa.String(length=80), nullable=True, comment='手机号'),
    sa.Column('birthday', sa.String(length=50), nullable=True, comment='生日'),
    sa.Column('height', sa.String(length=50), nullable=True, comment='身高'),
    sa.Column('eduStatus', sa.SmallInteger(), nullable=True, comment='教育状态 1-在读 2-已毕业'),
    sa.Column('bestEdu', sa.String(length=20), nullable=True, comment='最高学历'),
    sa.Column('email', sa.String(length=50), nullable=True, comment='邮箱'),
    sa.Column('qqNum', sa.String(length=20), nullable=True, comment='QQ'),
    sa.Column('weChat', sa.String(length=50), nullable=True, comment='微信号'),
    sa.Column('loginName', sa.String(length=50), nullable=True, comment='登录名'),
    sa.Column('password', sa.String(length=210), nullable=True, comment='登录密码'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loginName'),
    comment='305 用户表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
