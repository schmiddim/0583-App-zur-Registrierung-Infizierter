"""init

Revision ID: 2d547b718332
Revises: 3cd17252875c
Create Date: 2020-03-21 13:33:34.638415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d547b718332'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.Text(), nullable=True),
    sa.Column('lastname', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('phone_number', sa.Text(), nullable=True),
    sa.Column('case_number', sa.Text(), nullable=True),
    sa.Column('covid_status', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_persons'))
    )
  #  op.drop_index('my_index', table_name='models')
   # op.drop_table('models')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_models')
    )
   # op.create_index('my_index', 'models', ['name'], unique=1)
    op.drop_table('persons')
    # ### end Alembic commands ###
