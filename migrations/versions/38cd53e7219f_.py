"""empty message

Revision ID: 38cd53e7219f
Revises: 762402052503
Create Date: 2021-02-23 23:15:14.178731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38cd53e7219f'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=80), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
