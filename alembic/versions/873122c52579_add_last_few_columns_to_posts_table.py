"""add last few columns to posts table

Revision ID: 873122c52579
Revises: a978a6505300
Create Date: 2022-04-27 11:53:17.436248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '873122c52579'
down_revision = 'a978a6505300'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass