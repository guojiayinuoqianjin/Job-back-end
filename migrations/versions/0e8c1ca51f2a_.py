"""empty message

Revision ID: 0e8c1ca51f2a
Revises: 1fa16ee86342
Create Date: 2020-04-22 14:38:55.581262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e8c1ca51f2a'
down_revision = '1fa16ee86342'
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
