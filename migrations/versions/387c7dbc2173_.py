"""empty message

Revision ID: 387c7dbc2173
Revises: fedf0b9352f5
Create Date: 2021-12-27 12:47:45.051881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387c7dbc2173'
down_revision = 'fedf0b9352f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###