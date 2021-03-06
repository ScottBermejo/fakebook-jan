"""removed title column from Post

Revision ID: 89f1b0524482
Revises: d2b4664a81aa
Create Date: 2021-02-15 11:55:11.570669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89f1b0524482'
down_revision = 'd2b4664a81aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
