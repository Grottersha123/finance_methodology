import asyncio
from asyncio import sleep
import pandas as pd
import asyncpg
import os

from sshtunnel import SSHTunnelForwarder

from sql_query import raw_sql

tables = ['fk_form_0503721', 'fk_form_0503730_r1', 'fk_form_0503730_r2', 'fk_form_0503737_r1', 'fk_form_0503737_r2', 'fk_form_0503737_r3', 'fk_form_0503737_r4', 'fk_form_0503738', 'fk_form_0503768', 'fk_form_0503769_r1', 'fk_form_0503769_r2', 'fk_form_0503772_r1', 'fk_form_0503772_r2', 'fk_form_0503773_r1', 'fk_form_0503773_r2', 'fk_form_0503779']
result = []
clm = ['id', 'max', 'year', 'name_table', 'max', 'max']

df_data = pd.DataFrame(columns=clm)
ids = "001Ч1271|001Ц3401|001U9286|001У8228|001Ц7392|001Ц6399|001Ц1163|001U9481"
ids_lst = ids.split('|')
async def main(year='01012021',id=ids):
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
        server.start()
        sleep(2)
        local_port = str(server.local_bind_port)
        conn = await asyncpg.connect('postgresql://postgres:Sae7ZaeWklS@localhost:' + local_port + '/data')
        try:
        # connect to PostgreSQL
            for table in tables[:10]:
                sql_raw = """select
                                         substring(blocksubbo_codesub from 6 for 8) as id,
                                         max(blocksubbo_foname),
                                         '{0}' AS year,
                                         '{1}' as name_table,
                                         max(period),
                                         max(blocktypereport_id)
                                        from  {1}
                                        where
                                         period in ('{0}')
                                        and blocksubbo_codesub SIMILAR TO '%({2})%'
                                        group by substring(blocksubbo_codesub from 6 for 8)
                """.format(year, table, id)
                row = await conn.fetch(sql_raw)
                data = [[j for j in i] for i in row]
                data_ids = [i[0] for i in data]
                for ind, i in enumerate(id.split('|')):
                    if i not in data_ids:
                        data.append([i, None, year, table, None, None])
                result.extend(data)
                # Close the connection.
        except Exception as e:
            raise Exception("has error '%s'" % (e))
        finally:
            await conn.close()
        await conn.close()
        server.close()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(main(year='01012020')),
        loop.create_task(main(year="01012021")),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(result)
    pd.DataFrame(data=result, columns=clm).to_csv('{}.csv'.format('report'))

