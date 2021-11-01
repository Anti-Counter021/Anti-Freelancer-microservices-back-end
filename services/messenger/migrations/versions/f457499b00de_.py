"""empty message

Revision ID: f457499b00de
Revises: 4d1b3f2f4f11
Create Date: 2021-11-01 15:27:09.464911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f457499b00de'
down_revision = '4d1b3f2f4f11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_dialog')
    op.add_column('dialog', sa.Column('users_ids', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dialog', 'users_ids')
    op.create_table('user_dialog',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('dialog_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['dialog_id'], ['dialog.id'], name='user_dialog_dialog_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='user_dialog_pkey')
    )
    # ### end Alembic commands ###
