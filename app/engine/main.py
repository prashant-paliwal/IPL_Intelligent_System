from app.engine.commentary import generate_commentary
from app.engine.context import update_context
from app.engine.insight import generate_insight


async def process_event(e):
    ctx = update_context(e)

    comment = generate_commentary(e)
    insight = generate_insight(ctx)

    return {
        "commentary": comment,
        "insight": insight
    }