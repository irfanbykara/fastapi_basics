"""create posts table

Revision ID: d6896110d40a
Revises: 
Create Date: 2022-04-27 10:35:19.547243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6896110d40a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,
                                      primary_key=True),
                    sa.Column('title',sa.String(),nullable=False))




def downgrade():
    op.drop_table('posts')
