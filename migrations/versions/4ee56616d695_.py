"""empty message

Revision ID: 4ee56616d695
Revises: 
Create Date: 2018-05-27 00:55:25.628836

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ee56616d695'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', mysql.BIGINT(display_width=20), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('createtime', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
