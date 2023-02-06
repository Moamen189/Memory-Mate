"""make name nonuunique in useraface

Revision ID: 58f09616def9
Revises: f4a1f99c04d9
Create Date: 2023-02-02 15:25:43.971056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58f09616def9'
down_revision = 'f4a1f99c04d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userfaces', schema=None) as batch_op:
        batch_op.drop_constraint('userfaces_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userfaces', schema=None) as batch_op:
        batch_op.create_unique_constraint('userfaces_name_key', ['name'])

    # ### end Alembic commands ###