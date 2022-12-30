"""add extensive_coverage parameter

Revision ID: 71095b8e6343
Revises: 66cd6054c2d0
Create Date: 2022-12-12 13:36:08.659682

"""
import sqlalchemy as sa

from alembic import op
from app.models import ValidationSchema

# revision identifiers, used by Alembic.
revision = "71095b8e6343"
down_revision = "4272d0a43ff1"
branch_labels = None
depends_on = None

enum_name = "validation_type"
enum_keys_to_add = [ValidationSchema.extensive_coverage.name]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    for v in enum_keys_to_add:
        op.execute(f"ALTER TYPE {enum_name} ADD VALUE '{v}'")

    op.add_column(
        "jobs", sa.Column("extensive_coverage", sa.INTEGER(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    for v in enum_keys_to_add:
        sql = f"""DELETE FROM pg_enum
            WHERE enumlabel = '{v}'
            AND enumtypid = (
              SELECT oid FROM pg_type WHERE typname = '{enum_name}'
            )"""
        op.execute(sql)
    op.drop_column("jobs", "extensive_coverage")
    # ### end Alembic commands ###
