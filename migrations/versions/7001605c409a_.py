"""empty message

Revision ID: 7001605c409a
Revises: 75c41d029df0
Create Date: 2020-04-13 15:09:00.529125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7001605c409a'
down_revision = '75c41d029df0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_signup', sa.Column('userId', sa.BigInteger(), nullable=True, comment='申请学生的id号'))
    op.drop_column('job_signup', 'stuId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_signup', sa.Column('stuId', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True, comment='申请学生的id号'))
    op.drop_column('job_signup', 'userId')
    # ### end Alembic commands ###
