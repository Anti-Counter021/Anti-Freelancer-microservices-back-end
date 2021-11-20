"""empty message

Revision ID: 07666d2cdc2f
Revises: 9fd2ab829470
Create Date: 2021-11-20 14:30:33.452911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07666d2cdc2f'
down_revision = '9fd2ab829470'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('appraisal', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###
