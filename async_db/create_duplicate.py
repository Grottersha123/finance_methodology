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
clm = ['table_name', 'group_by', 'not_group_by']

df_data = pd.DataFrame(columns=clm)
ids_lst = ids.split('|')


def create_sql_str(table):
    sql_raw = """select '{0}' as table_name,count(str)
                                from
                                (select rtrim(ltrim(replace({0}::text, ',', ''), '('), ')') as str from {0} group by str) as t""".format(table)
    return sql_raw


def create_sql(table):
    sql_raw = """select count(str)
                                from
                                (select rtrim(ltrim(replace({0}::text, ',', ''), '('), ')') as str from {0}) as t""".format(table)
    return sql_raw




async def main(tables=tables):
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    # Execute a statement to create a new table.
    print('start')
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
                    sql_raw_str = create_sql_str(table)

                    row_str = await conn.fetch(sql_raw_str)

                    sql_raw_str = create_sql(table)
                    row = await conn.fetch(sql_raw_str)
                    data_str = [[j for j in i] for i in row_str]
                    data = [[j for j in i] for i in row]
                    print(data_str[0]+data[0])

                    result.extend([data_str[0]+data[0]])
                    logging.info(table)
                    # Close the connection.
            except Exception as e:
                print(e)
                raise Exception("has error '%s'" % e)
            finally:
                print('connect')
                await conn.close()
            await conn.close()
            server.close()
    if os.name == 'posix':
        conn = await asyncpg.connect('postgresql://postgres:Sae7ZaeWklS@10.10.59.238:' + "5432" + '/data')
        try:
            # connect to PostgreSQL
            for table in tables[:]:
                sql_raw_str = create_sql(table)
                row = await conn.fetch(sql_raw_str)
                data_str = [[j for j in i] for i in row_str]
                data = [[j for j in i] for i in row]
                print(data_str[0] + data[0])
                logging.info(table)
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
        loop.create_task(main(tables=tables[:4])),
        loop.create_task(main(tables=tables[4:8])),
        loop.create_task(main(tables=tables[8:12])),
        loop.create_task(main(tables=tables[12:16])),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('save csv report')
    print(result)
    pd.DataFrame(data=result, columns=clm).to_csv('{}.csv'.format('report_dblicate'))
