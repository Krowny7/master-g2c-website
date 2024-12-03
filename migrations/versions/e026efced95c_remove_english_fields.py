"""remove english fields

Revision ID: e026efced95c
Revises: 531cf84f0268
Create Date: 2024-12-02 23:20:54.980907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e026efced95c'
down_revision = '531cf84f0268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('title_en')
        batch_op.drop_column('description_en')

    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.drop_column('title_en')
        batch_op.drop_column('content_en')

    with op.batch_alter_table('ranking', schema=None) as batch_op:
        batch_op.drop_column('category_en')

    with op.batch_alter_table('teacher', schema=None) as batch_op:
        batch_op.drop_column('title_en')
        batch_op.drop_column('description_en')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teacher', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_en', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.VARCHAR(length=200), nullable=True))

    with op.batch_alter_table('ranking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_en', sa.VARCHAR(length=200), nullable=True))

    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content_en', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.VARCHAR(length=200), nullable=True))

    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_en', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###
