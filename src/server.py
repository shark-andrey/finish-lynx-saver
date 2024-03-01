import asyncio

from logger import logger


async def main(port):
    server = await asyncio.start_server(
        client_connected_cb=on_accept,
        host="0.0.0.0",
        port=port,
        reuse_address=True
    )
    async with server:
        await server.serve_forever()
        
        
async def on_accept(reader, writer):
    while True:
        message = await reader.readline()
        try:
            message = message.decode().strip()
        except UnicodeDecodeError:
            logger.error("Error decoding message: {message}")
            continue
        if len(message) > 0:
            logger.debug(f"Message: {message}")
            try:
                await handle_message(message)
            except Exception as e:
                logger.error(f"{e}")
                
                
async def handle_message(message: str):
    records: list[Record] = Record.parse(message)
    if len(records) > 0:
        await upsert_records(records)
    
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finish")
    parser.add_argument("--port", type=int, default=10000)
    args = parser.parse_args()
    asyncio.run(main(args.port))
