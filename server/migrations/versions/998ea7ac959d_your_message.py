"""your message

Revision ID: 998ea7ac959d
Revises: 
Create Date: 2024-10-10 13:37:40.968972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998ea7ac959d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
