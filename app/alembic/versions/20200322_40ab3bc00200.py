"""Adding person creation and update date

Revision ID: 40ab3bc00200
Revises: 2d547b718332
Create Date: 2020-03-22 10:59:07.645291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40ab3bc00200'
down_revision = '2d547b718332'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('persons', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('persons', sa.Column('date_updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###

def downgrade():
    op.drop_column('persons', 'date_updated')
    op.drop_column('persons', 'date_created')
    # ### end Alembic commands ###
