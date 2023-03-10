"""Add table Photo

Revision ID: a34255a34302
Revises: e263fd2a8c1e
Create Date: 2023-01-01 01:19:29.314646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a34255a34302'
down_revision = 'e263fd2a8c1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_path', sa.String(), nullable=False))
        batch_op.drop_column('photos_path')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photos_path', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('photo_path')

    # ### end Alembic commands ###
