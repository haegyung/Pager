"""added status column to user

Revision ID: 11d26e86341a
Revises: 58533af39fd7
Create Date: 2013-02-07 17:28:05.493480

"""

# revision identifiers, used by Alembic.
revision = '11d26e86341a'
down_revision = '58533af39fd7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'users',
        sa.Column(
            'status', sa.Integer(),
            nullable=False, server_default='0', index=True
        )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    ### end Alembic commands ###
