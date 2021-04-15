from asyncio import sleep
import timeit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sshtunnel import SSHTunnelForwarder
import multiprocessing
from sql_query import raw_sql
table = ['fk_form_0503721', 'fk_form_0503730_r1', 'fk_form_0503730_r2', 'fk_form_0503737_r1', 'fk_form_0503737_r2',
         'fk_form_0503737_r3', 'fk_form_0503737_r4', 'fk_form_0503738', 'fk_form_0503768', 'fk_form_0503769_r1',
         'fk_form_0503769_r2', 'fk_form_0503772_r1', 'fk_form_0503772_r2', 'fk_form_0503773_r1', 'fk_form_0503773_r2',
         'fk_form_0503779']

periods = ['01012020', '01012021']
ids = ['001Ч1271', '001Ц3401', '001U9286', '001У8228', '001Ц7392', '001Ц6399', '001Ц1163', '001U9481']

def runQuery(query):
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

        # connect to PostgreSQL
        local_port = str(server.local_bind_port)
        engine = create_engine('postgresql://postgres:Sae7ZaeWklS@localhost:' + local_port + '/data')
        Session = sessionmaker(bind=engine)
        session = Session()
        start = timeit.default_timer()
        for i in query:
            records = session.execute(i)
            records = records.fetchall()
            print("Total rows are:  ", len(records))
        stop = timeit.default_timer()
        print(stop - start)
        session.close()
        server.stop()
if __name__ == '__main__':
    print(len(raw_sql))
    pool = multiprocessing.Pool(4)
    start = timeit.default_timer()

    for i in pool.imap_unordered(runQuery, [raw_sql[raw_:raw_+10] for raw_ in range(0, len(raw_sql), 10)]):
        continue
    pool.close()
    stop = timeit.default_timer()
    print(stop - start)
    start = timeit.default_timer()
    runQuery(raw_sql)
    stop = timeit.default_timer()
    print(stop - start)

    pool = multiprocessing.Pool(24)
    start = timeit.default_timer()

    for i in pool.imap_unordered(runQuery, [raw_sql[raw_:raw_ + 10] for raw_ in range(0, len(raw_sql), 10)]):
        continue
    pool.close()
    stop = timeit.default_timer()
    print(stop - start)







