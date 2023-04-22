"""empty message

Revision ID: 0a55ac4bf0dc
Revises: a5317d3a2652
Create Date: 2023-04-21 14:20:13.693280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a55ac4bf0dc'
down_revision = 'a5317d3a2652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('index_web')
    with op.batch_alter_table('promote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link_pro2', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promote', schema=None) as batch_op:
        batch_op.drop_column('link_pro2')

    op.create_table('index_web',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('link_i', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('title_i', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('author_i', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='index_web_pkey')
    )
    # ### end Alembic commands ###