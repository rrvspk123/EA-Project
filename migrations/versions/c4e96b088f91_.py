"""empty message

Revision ID: c4e96b088f91
Revises: 249a99c3c7f9
Create Date: 2023-04-22 03:32:41.413455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4e96b088f91'
down_revision = '249a99c3c7f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('website', schema=None) as batch_op:
        batch_op.alter_column('middle_data',
               existing_type=sa.VARCHAR(length=3000),
               type_=sa.String(length=10000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('website', schema=None) as batch_op:
        batch_op.alter_column('middle_data',
               existing_type=sa.String(length=10000),
               type_=sa.VARCHAR(length=3000),
               existing_nullable=True)

    # ### end Alembic commands ###