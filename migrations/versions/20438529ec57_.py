"""empty message

Revision ID: 20438529ec57
Revises: c4e96b088f91
Create Date: 2023-04-22 05:04:18.626366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20438529ec57'
down_revision = 'c4e96b088f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_tab',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_w', sa.String(length=100), nullable=True),
    sa.Column('link_w', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('web_tab')
    # ### end Alembic commands ###