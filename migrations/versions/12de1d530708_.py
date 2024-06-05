"""empty message

Revision ID: 12de1d530708
Revises: 8e15b945c7e9
Create Date: 2024-06-05 14:41:16.099304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12de1d530708'
down_revision = '8e15b945c7e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diary', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weather', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diary', schema=None) as batch_op:
        batch_op.drop_column('weather')

    # ### end Alembic commands ###
