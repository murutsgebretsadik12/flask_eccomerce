"""update immigration

Revision ID: 200b232dcafa
Revises: 47cf1f7c7773
Create Date: 2024-04-01 09:33:32.756937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '200b232dcafa'
down_revision = '47cf1f7c7773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_data', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('image_data')

    # ### end Alembic commands ###