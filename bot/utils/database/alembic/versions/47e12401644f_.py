"""empty message

Revision ID: 47e12401644f
Revises: 
Create Date: 2024-11-07 09:23:17.292024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47e12401644f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arcViews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('viewID', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guildSettings',
    sa.Column('guildID', sa.BigInteger(), nullable=False),
    sa.Column('serverJoin', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('ownerID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('guildID'),
    sa.UniqueConstraint('guildID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guildSettings')
    op.drop_table('arcViews')
    # ### end Alembic commands ###
