"""empty message

Revision ID: 70d74884cca9
Revises: 47e12401644f
Create Date: 2024-11-21 15:55:52.128068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70d74884cca9'
down_revision: Union[str, None] = '47e12401644f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('worth', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.add_column('guildSettings', sa.Column('userAmount', sa.Integer(), nullable=True))
    op.add_column('guildSettings', sa.Column('economy', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'guildSettings', ['guildID'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'guildSettings', type_='unique')
    op.drop_column('guildSettings', 'economy')
    op.drop_column('guildSettings', 'userAmount')
    op.drop_table('Users')
    # ### end Alembic commands ###