"""
Async iterators example 8: Async iteration in concurrent code.
"""
import threading
from pathlib import Path
import re
import aiofiles
import argparse
import asyncio
import logging
import time
import aiohttp

LOG = logging.getLogger("examples")

URL_PATTERN = r"(https:\/\/(www\.)?)(.+)\.(com|org|dev)"


class AsyncFileIterator:
    def __init__(self, path):
        self.path = path
        self.file = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.file is None:
            LOG.info(f"AsyncFileIterator: Opening {self.path}")
            self.file = await aiofiles.open(self.path, mode="r")
        line = await self.file.readline()
        if not line:
            LOG.info(f"AsyncFileIterator: Closing {self.path}")
            await self.file.close()
            raise StopAsyncIteration
        LOG.info(f"AsyncFileIterator: returning line \"{line.strip()}\"")
        return line


async def consume(name: int, q: asyncio.Queue) -> None:
    """
    Consumer.
    :param name: Consumer's name.
    :param q: Queue
    :return: None.
    """
    consumer_id = f"{name}-{threading.current_thread().name}"
    LOG.info(f"[{consumer_id}] Consumer starting")
    directory = Path.cwd()
    output_dir = directory / "examples/async_iterators/data"

    while True:
        LOG.info(f"[{consumer_id}] waiting for next element to read")
        url, t = await q.get()
        LOG.info(f"[{consumer_id}] read Q element {url}")
        timeout_seconds = 60
        session_timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        try:
            async with aiohttp.ClientSession(timeout=session_timeout) as session:
                LOG.info(f"[{consumer_id}] connecting to {url}, with total timeout {timeout_seconds} secs")
                async with session.get(url) as resp:
                    resp.raise_for_status()
                    LOG.info(f"[{consumer_id}] Got response from {url}")
                    response_text = await resp.text()
                    match = re.search(URL_PATTERN, url)
                    site_name = match.group(3)
                    if match is None or site_name is None:
                        LOG.error(f"[{consumer_id}] URL {url} does not regex match \"{URL_PATTERN}\"")
                    else:
                        output_path = output_dir / f"{site_name}.html"
                        LOG.info(f"[{consumer_id}] Writing to {output_path}")
                        async with aiofiles.open(output_path, "w") as f:
                            await f.write(response_text)
        except aiohttp.ClientConnectorError as e:
            LOG.error(f"[{consumer_id}] Connection error with {url}: {str(e)}")

        now = time.perf_counter()
        LOG.info(f"[{consumer_id}] Q element <{url}> processed {now - t:0.5f} seconds after queueing.")
        q.task_done()


async def run_example():
    thread_name = f"{threading.current_thread().name}"
    directory = Path.cwd()
    LOG.info(f"[{thread_name}] Current directory: {directory}")
    web_sites_file = directory / "examples/async_iterators/data/websites.txt"
    async_iter = AsyncFileIterator(web_sites_file)

    # Create a queue to communicate the urls to the tasks which will connect to them.
    q = asyncio.Queue()

    # Start the consumers
    # Create the consumers
    # Experiment with different values and assess the overall performance gains
    tasks_count = 5
    LOG.info(f"[{thread_name}] Create %d consumers", tasks_count)
    consumers = [asyncio.create_task(consume(n, q)) for n in range(tasks_count)]

    async for next_url in async_iter:
        url = str(next_url).strip()
        if len(url) > 0:
            if url.startswith("#"):
                LOG.debug(f"[{thread_name}] Producer: skipping comment \"{url}\"")
            else:
                LOG.info(f"[{thread_name}] Producer: URL: {url}")
                t = time.perf_counter()
                await q.put((url, t))
        else:
            LOG.warning(f"[{thread_name}] Producer: No URL provided: \"{next_url}\"")

    # Wait for all messages to be read.
    # Implicitly awaits consumers, too.
    LOG.info(f"[{thread_name}] Waiting for all messages to be processed...")
    await q.join()
    LOG.info(f"[{thread_name}] All messages have been processed.")

    # Cancel all consumers
    LOG.info(f"[{thread_name}] Cancelling all consumers...")
    for c in consumers:
        c.cancel()

    LOG.info(f"[{thread_name}] Done.")


def example_10(args: argparse.Namespace) -> None:
    """
    Run example 10
    """
    LOG.info("Running async iterators example 10 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
