"""create trades and predictions tables

Revision ID: 0001
Revises: 
Create Date: 2024-07-01
"""
from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'trades',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('symbol', sa.String(16)),
        sa.Column('action', sa.String(8)),
        sa.Column('amount', sa.Float),
        sa.Column('price', sa.Float),
        sa.Column('timestamp', sa.DateTime, server_default=sa.func.now()),
    )
    op.create_table(
        'predictions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('input', sa.JSON),
        sa.Column('trend', sa.String(8)),
        sa.Column('confidence', sa.Float),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('predictions')
    op.drop_table('trades') 