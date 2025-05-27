from sqlalchemy import text
from database import engine

def get_spending_by_category(user_id):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT category, SUM(amount) as total_spent
            FROM transactions
            WHERE user_id = :user_id
            GROUP BY category
        """), {"user_id": user_id})
        return {row['category']: row['total_spent'] for row in result}

def compare_budget_vs_spending(user_budget, actual_spending):
    result = {}
    for category, planned in user_budget.items():
        spent = actual_spending.get(category, 0)
        result[category] = {
            "planned": planned,
            "spent": spent,
            "difference": planned - spent
        }
    return result