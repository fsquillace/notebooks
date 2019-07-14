async def _wrap_coro(sem, coro):
    # Semaphore limits num of concurrent I/O
    async with sem:
        return await coro


async def _run_until_complete(coros, limit):
    sem = asyncio.Semaphore(limit)
    futures = [
        _wrap_coro(sem, coro)
        for coro in coros
    ]
    return await asyncio.wait(futures)


def run_until_complete(coros, limit=None, loop=None):
    if limit is None:
        limit = len(coros)
    if loop is None:
        loop = asyncio.get_event_loop()

    return loop.run_until_complete(_run_until_complete(coros, limit=limit))
