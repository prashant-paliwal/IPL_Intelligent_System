# run_consumer.py
import asyncio
from app.stream.consumer import consume

asyncio.run(consume())