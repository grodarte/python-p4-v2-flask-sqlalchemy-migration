"""rename department

Revision ID: af99a08d2f5e
Revises: f2a72a3920c8
Create Date: 2025-03-28 14:14:08.177847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af99a08d2f5e'
down_revision = 'f2a72a3920c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
