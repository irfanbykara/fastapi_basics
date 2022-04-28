"""add phone number

Revision ID: 46dffedbbce7
Revises: fffcfbb5f285
Create Date: 2022-04-28 09:29:46.515784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46dffedbbce7'
down_revision = 'fffcfbb5f285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
