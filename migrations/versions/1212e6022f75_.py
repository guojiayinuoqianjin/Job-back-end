"""empty message

Revision ID: 1212e6022f75
Revises: 68702b2d54e3
Create Date: 2020-04-19 13:51:57.180954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1212e6022f75'
down_revision = '68702b2d54e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uId', sa.BigInteger(), nullable=True, comment='关联的用户id'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_column('uId')

    # ### end Alembic commands ###
