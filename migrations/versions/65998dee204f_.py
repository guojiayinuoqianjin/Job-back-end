"""empty message

Revision ID: 65998dee204f
Revises: b611d1d3c78f
Create Date: 2020-04-22 14:40:03.266184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65998dee204f'
down_revision = 'b611d1d3c78f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_signup', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isVerify', sa.SmallInteger(), nullable=True, comment='是否通过 1-通过 2-不通过'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_signup', schema=None) as batch_op:
        batch_op.drop_column('isVerify')

    # ### end Alembic commands ###
