import asyncio
import logging
from asyncio import sleep
import pandas as pd
import asyncpg
import os
from async_db.id_org import ids
from sshtunnel import SSHTunnelForwarder

logging.getLogger().setLevel(logging.INFO)

tables = ['fk_form_0503721', 'fk_form_0503730_r1',
          'fk_form_0503730_r2',
          'fk_form_0503737_r1', 'fk_form_0503737_r2',
          'fk_form_0503737_r3', 'fk_form_0503737_r4',
          'fk_form_0503738', 'fk_form_0503768',
          'fk_form_0503769_r1',
          'fk_form_0503769_r2', 'fk_form_0503772_r1',
          'fk_form_0503772_r2', 'fk_form_0503773_r1',
          'fk_form_0503773_r2',
          'fk_form_0503779']
result = []
clm = ['id', 'max', 'year', 'name_table', 'last_date', 'max_report_type','rows_num']

df_data = pd.DataFrame(columns=clm)
ids_lst = ids.split('|')


def create_sql(year, table, id_set):
    sql_raw = """select 
                                        substring(blocksubbo_codesub from 6 for 8) as id,
                                        max(blocksubbo_foname),
                                        '{0}' AS year,
                                        '{1}' as name_table,
                                        max(period) as last_date,
                                        max(blocktypereport_id) as max_report_type,
                                        count(id) as rows_num
                                       from {1} 
                                       where 
                                        period in ('{0}')
                                       and blocksubbo_codesub SIMILAR TO '%({2})%'
                                       group by substring(blocksubbo_codesub from 6 for 8)""".format(year, table,
                                                                                                     id_set)
    return sql_raw




async def main(year='01012021', id_set=ids, tables=tables):
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    # Execute a statement to create a new table.
    if os.name == 'nt':
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
                for table in tables[:]:
                    sql_raw = create_sql(year, table, id_set)
                    row = await conn.fetch(sql_raw)
                    data = [[j for j in i] for i in row]
                    data_ids = [i[0] for i in data]
                    for ind, i in enumerate(id_set.split('|')):
                        if i not in data_ids:
                            data.append([i, None, year, table, None, None])
                    result.extend(data)
                    logging.info(table)
                    # Close the connection.
            except Exception as e:
                raise Exception("has error '%s'" % e)
            finally:
                await conn.close()
            await conn.close()
            server.close()
    if os.name == 'posix':
        conn = await asyncpg.connect('postgresql://postgres:Sae7ZaeWklS@10.10.59.238:' + "5432" + '/data')
        try:
            # connect to PostgreSQL
            for table in tables[:]:
                sql_raw = create_sql(year, table, id_set)
                row = await conn.fetch(sql_raw)
                data = [[j for j in i] for i in row]
                data_ids = [i[0] for i in data]
                for ind, i in enumerate(id_set.split('|')):
                    if i not in data_ids:
                        data.append([i, None, year, table, None, None])
                logging.info(table)
                result.extend(data)
                # Close the connection.
        except Exception as e:
            pd.DataFrame(data=result, columns=clm).to_csv('{}.csv'.format('report_error'))
            raise Exception("has error '%s'" % e)
        finally:
            await conn.close()
        await conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(main(year='01012020', tables=tables[:8])),
        loop.create_task(main(year='01012020', tables=tables[8:16])),
        loop.create_task(main(year="01012021", tables=tables[:8])),
        loop.create_task(main(year="01012021", tables=tables[8:16]))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    pd.DataFrame(data=result, columns=clm).to_csv('{}.csv'.format('report'))
