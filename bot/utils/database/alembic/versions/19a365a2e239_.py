"""empty message

Revision ID: 19a365a2e239
Revises: 
Create Date: 2024-11-29 11:56:11.988095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19a365a2e239'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('worth', sa.Integer(), nullable=True),
    sa.Column('messagesSent', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('guildSettings',
    sa.Column('guildID', sa.BigInteger(), nullable=False),
    sa.Column('serverJoin', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('ownerID', sa.Integer(), nullable=True),
    sa.Column('userAmount', sa.Integer(), nullable=True),
    sa.Column('economy', sa.Integer(), nullable=True),
    sa.Column('economyLeft', sa.Integer(), nullable=True),
    sa.Column('defacedCurrenty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('guildID'),
    sa.UniqueConstraint('guildID')
    )
    op.create_table('Economy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('coins', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['Users.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Levels',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('exp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['Users.uid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('arcViews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('viewID', sa.BigInteger(), nullable=True),
    sa.Column('guildID', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['guildID'], ['guildSettings.guildID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arcViews')
    op.drop_table('Levels')
    op.drop_table('Economy')
    op.drop_table('guildSettings')
    op.drop_table('Users')
    # ### end Alembic commands ###
