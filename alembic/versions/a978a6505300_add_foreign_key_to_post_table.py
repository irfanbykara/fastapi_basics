"""add foreign key to post table

Revision ID: a978a6505300
Revises: e2664976640a
Create Date: 2022-04-27 11:48:36.869666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a978a6505300'
down_revision = 'e2664976640a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),
                                   nullable=False))
    op.create_foreign_key('posts_users_fk',
                          source_table="posts",
                          referent_table="users",
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete="CASCADE")


def downgrade():
    op.drop_constraint("posts_users_fk",table_name="posts")
    op.drop_column('posts','owner_id')
