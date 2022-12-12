"""Add in certified_by_name to affiliation.

Revision ID: 7e3f009cb4ae
Revises: b80bbb12beda
Create Date: 2022-11-16 18:45:50.340278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e3f009cb4ae'
down_revision = 'b80bbb12beda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('affiliations', sa.Column('certified_by_name', sa.String(length=100), nullable=True))
    op.add_column('affiliations_version', sa.Column('certified_by_name', sa.String(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('affiliations_version', 'certified_by_name')
    op.drop_column('affiliations', 'certified_by_name')
    # ### end Alembic commands ###