"""empty message

Revision ID: 22493872e5f1
Revises: 
Create Date: 2019-05-26 22:21:16.536299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22493872e5f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('client', sa.String(length=60), nullable=True),
    sa.Column('client_priority', sa.Integer(), nullable=False),
    sa.Column('target_date', sa.DateTime(), nullable=False),
    sa.Column('product_areas', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature')
    op.drop_table('client')
    # ### end Alembic commands ###
