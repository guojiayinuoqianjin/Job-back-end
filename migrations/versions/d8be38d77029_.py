"""empty message

Revision ID: d8be38d77029
Revises: d9307a4c2810
Create Date: 2020-04-22 19:56:19.135543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8be38d77029'
down_revision = 'd9307a4c2810'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('com_sign', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isVerify', sa.SmallInteger(), nullable=True, comment='是否通过审核 1-提交待审核 2-通过 3-不通过'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('com_sign', schema=None) as batch_op:
        batch_op.drop_column('isVerify')

    # ### end Alembic commands ###
