"""change price to string

Revision ID: 7f49276579f8
Revises: 0647e679a9ad
Create Date: 2021-04-24 00:17:03.867017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f49276579f8'
down_revision = '0647e679a9ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(precision=4),
               type_=sa.String(length=5),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.String(length=5),
               type_=sa.NUMERIC(precision=4),
               existing_nullable=True)

    # ### end Alembic commands ###
