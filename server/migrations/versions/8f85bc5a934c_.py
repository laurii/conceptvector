"""empty message

Revision ID: 8f85bc5a934c
Revises: 9c72e6d45ffa
Create Date: 2016-03-20 08:36:43.990315

"""

# revision identifiers, used by Alembic.
revision = '8f85bc5a934c'
down_revision = '9c72e6d45ffa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('asset_id', sa.BIGINT(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'asset_id')
    ### end Alembic commands ###
