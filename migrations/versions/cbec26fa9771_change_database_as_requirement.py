"""change database as requirement

Revision ID: cbec26fa9771
Revises: cbfbb67a7351
Create Date: 2022-12-16 20:58:40.105627

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cbec26fa9771'
down_revision = 'cbfbb67a7351'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    op.drop_table('locations')
    op.drop_table('agenda')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('photo_path', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('user_type', sa.Enum('PATIENT', 'CAREGIVER', name='eusertype'), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('date_of_birth', sa.Date(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=80),
               nullable=False)
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('type')
        batch_op.drop_column('hashed_password')
        batch_op.drop_column('bio')
        batch_op.drop_column('age')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('hashed_password', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('type', postgresql.ENUM('PATIENT', 'CAREGIVER', name='eusertype'), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('phone')
        batch_op.drop_column('user_type')
        batch_op.drop_column('photo_path')
        batch_op.drop_column('password')
        batch_op.drop_column('username')

    op.create_table('agenda',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('occasion', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='agenda_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='agenda_pkey')
    )
    op.create_table('locations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('lang', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='locations_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='locations_pkey')
    )
    op.create_table('notifications',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='notifications_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='notifications_pkey')
    )
    # ### end Alembic commands ###