import asyncio
from asyncio import sleep

import asyncpg
import os

from sshtunnel import SSHTunnelForwarder

from sql_query import raw_sql


async def main(ids='001Ч1271|001Ц3401|001U9286|001У8228|001Ц7392|001Ц6399|001Ц1163|001U9481'):
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    # Execute a statement to create a new table.
    with SSHTunnelForwarder(
            ('193.41.140.35', 22003),  # Remote server IP and SSH port
            ssh_username="analit",
            ssh_password="Sae7ZaeW",
            remote_bind_address=(
                    'localhost', 5432)) as server:
        # PostgreSQL server IP and sever port on remote machine
        server.daemon_forward_servers = True
        server.start()  # start ssh seve
        sleep(2)
        local_port = str(server.local_bind_port)
        conn = await asyncpg.connect('postgresql://postgres:Sae7ZaeWklS@localhost:' + local_port + '/data')

        # connect to PostgreSQL


        row = await conn.fetch("""

        """)
        print(len(row))
    # Close the connection.
        await conn.close()
if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(main())