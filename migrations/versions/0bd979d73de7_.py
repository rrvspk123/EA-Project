"""empty message

Revision ID: 0bd979d73de7
Revises: 20438529ec57
Create Date: 2023-04-22 06:49:41.455678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bd979d73de7'
down_revision = '20438529ec57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('web_tab', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attributes', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('web_tab', schema=None) as batch_op:
        batch_op.drop_column('attributes')

    # ### end Alembic commands ###