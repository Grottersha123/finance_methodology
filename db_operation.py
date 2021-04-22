from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  # Run pip install sqlalchemy
from sshtunnel import SSHTunnelForwarder  # Run pip install sshtunnel


def insert_data(res):
    try:
        with SSHTunnelForwarder(
                ('193.41.140.35', 22003),  # Remote server IP and SSH port
                ssh_username="analit",
                ssh_password="Sae7ZaeW",
                remote_bind_address=(
                'localhost', 5432)) as server:
            # PostgreSQL server IP and sever port on remote machine
            server.daemon_forward_servers = True
            server.start()  # start ssh seve
            print('start')
            # connect to PostgreSQL
            local_port = str(server.local_bind_port)
            engine = create_engine('postgresql://iacmon:WCVaB90x5@127.0.0.1:' + local_port + '/data')
            # op2_3_score where op
            Session = sessionmaker(bind=engine)
            session = Session()
            # test data retrieval
            for ind, d in enumerate(res):
                data, score = d[0], d[1]
                print(data, score)
                raw_str = """INSERT INTO dep_orgs_payment
                (blocksubbo_codesub, period,
                op1, op2, op3, op4, op5 , op6, op7, op8, op9,
                pfu3, pfu3a, pfu6,
                op1_score, op5_score,
                op7_score, op8_score, pfu3_score,
                pfu6_score, v1_score, v2_score, 
                pfu10, pfu11, pfu12, pfu13,
                pfu14, pfu15, lp3, lp5,
                pfu10_11_score, pfu12_13_score,
                pfu14_score, pfu15_score, lp3_score, lp5_score,v3_score, pfu4, pfu5, pfu7, pfu8, pfu9,
                op1a,
                op10a,
                op11a,
                op5a,
                op6a,
                op7a,
                op8a,
                op9a)
                VALUES ('{}', '2021-01-01 00:00:00.000000',
                {}, {}, {}, {}, {}, {}, {}, {},
                {}, {}, {},
                {}, {}, {},
                {}, {}, {},
                {}, {}, {}, 
                {},{}, {}, {},
                {}, {}, {}, {},
                {}, {},
                {}, {},{},{},{},
                {},{},{},{},{},
                {},{},{},{},{},{},{},{});""".\
                    format(data['id'],
                           data['op_1_d_t_delta'], data['op_2_d_t_max_value_21'], data['op_3_d_t_max_delta_max_percent'], data['op_4_p_t_delta'], data['op_5'], data['op_6'], data['op_7'], data['op_8'], data['op_9'],
                           data['pfu_3'], data['pfu_3a'], data['pfu_6'],
                           # score['op_2_score']
                           score['op_1_score'], score['op_5_score'],
                           score['op_7_score'], score['op_8_score'], score['pfu_3_score'],
                           score['pfu_6_score'], score['v_1_score'], score['v_2_score'],
                           data['pfu_10_oc_1'], data['pfu_11'], data['pfu_12_oc_2'], data['pfu_13'],
                           data['pfu_14'], data['pfu_15'], data['lp_3_ko_delta'], data['lp_5'],
                           score['pfu_10_score'], score['pfu_12_score'],  # Oleg - change: drop this duplicate score['v_2_score'],
                           score['pfu_14_score'], score['pfu_15_score'], score['lp_3_score'],
                           score['lp_5_score'], score['v_3_score'],
                           data['pfu_4'], data['pfu_5'], data['pfu_7'], data['pfu_8'], data['pfu_9'],

                           data['op_1a'], data['op_10a'], data['op_11a'], data['op_5a'], data['op_6a'],
                           data['op_7a'], data['op_8a'], data['op_9a']
                           )

                print('insert', ind, data['id'])
                test = session.execute(raw_str)

            session.commit()
            session.close()
            server.stop()
            return data['id']
    except Exception as e:
        print("Failed to insert record into mobile table", error)
        server.stop()


def insert_data_rfkm_no(res):
    with SSHTunnelForwarder(
            ('193.41.140.35', 22003),  # Remote server IP and SSH port
            ssh_username="analit",
            ssh_password="Sae7ZaeW",
            remote_bind_address=(
                    'localhost', 5432)) as server:
        # PostgreSQL server IP and sever port on remote machine
        server.daemon_forward_servers = True
        sleep(2)
        server.start()  # start ssh seve

        # connect to PostgreSQL
        local_port = str(server.local_bind_port)

        engine = create_engine('postgresql://postgres:Sae7ZaeWklS@localhost:' + local_port + '/data')
        Session = sessionmaker(bind=engine)
        session = Session()
        # test data retrieval
        for ind, d in enumerate(res):
            data, score = d[0], d[1]
            print(data, score)
            raw_str = """
            insert into dep_rkfm_no 
            (blocksubbo_codesub, period, pkp_1, pkp_2, pkp_3, pfu_1, pfu_2, pfu_3, pfu_5, pfu_6, pfu_7,
                     sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, dp_1, dp_2)
                     values ('{id}','2021-01-01 00:00:00.000000',{pkp_1}, {pkp_2}, {pkp_3}, {pfu_1}, {pfu_2}, {pfu_3}, {pfu_5}, {pfu_6}, {pfu_7}, {sp_1}, {sp_2}, {sp_3}, {sp_4}, {sp_5}, {sp_6}, {sp_7}, {dp_1}, {dp_2});""".format(
                data['id'], '2021-01-01 00:00:00.000000', **data)

            print(raw_str)

            print('insert', ind, data['id'])

            test = session.execute(raw_str)

        session.commit()
        session.close()
        server.stop()
        return data['id']
    # except ValueError as error:
    #     print("Failed to insert record into mobile table", error)
    #     server.stop()



def insert_data_rfkm_oovo(res):
    with SSHTunnelForwarder(
            ('193.41.140.35', 22003),  # Remote server IP and SSH port
            ssh_username="analit",
            ssh_password="Sae7ZaeW",
            remote_bind_address=(
                    'localhost', 5432)) as server:
        # PostgreSQL server IP and sever port on remote machine
        server.daemon_forward_servers = True
        sleep(2)
        server.start()  # start ssh seve

        # connect to PostgreSQL
        local_port = str(server.local_bind_port)

        engine = create_engine('postgresql://postgres:Sae7ZaeWklS@localhost:' + local_port + '/data')
        Session = sessionmaker(bind=engine)
        session = Session()
        # test data retrieval
        for ind, d in enumerate(res):
            data, score = d[0], d[1]
            print(data, score)
            raw_str = """
            insert into dep_rkfm_oovo (blocksubbo_codesub, pkp_1, pkp_2, pkp_3, pfu_1, pfu_2, pfu_3, pfu_4, pfu_5,
                           pfu_6, sp_1, sp_1a, sp_2, sp_2a, sp_3, sp_4, sp_5, pknpa_1, pknpa_2, pknpa_3, dp_1, pkp_1_score, 
                           pkp_2_score, pkp_3_score, pfu_1_score, pfu_2_score, pfu_3_score, pfu_4_score, pfu_5_score, 
                           pfu_6_score, sp_1_score, sp_1a_score, sp_2_score, sp_2a_score, sp_3_score, sp_4_score, 
                           sp_5_score, pknpa_1_score, pknpa_2_score, pknpa_3_score, dp_1_score, pkp_4, pkp_5, pkp_4_score, pkp_5_score)
                     values ('{id}',{pkp_1}, {pkp_2}, {pkp_3}, {pfu_1}, {pfu_2}, {pfu_3}, {pfu_4}, {pfu_5}, {pfu_6}, {sp_1}, {sp_1a}, 
                     {sp_2}, {sp_2a}, {sp_3}, {sp_4}, {sp_5}, {pknpa_1}, {pknpa_2}, {pknpa_3}, {dp_1}, {pkp_1_score},
                      {pkp_2_score}, {pkp_3_score}, {pfu_1_score}, {pfu_2_score}, {pfu_3_score}, {pfu_4_score}, 
                      {pfu_5_score}, {pfu_6_score}, {sp_1_score}, {sp_1a_score}, {sp_2_score}, {sp_2a_score}, 
                     {sp_3_score}, {sp_4_score}, {sp_5_score}, {pknpa_1_score}, {pknpa_2_score}, {pknpa_3_score}, {dp_1_score},
                     {pkp_4}, {pkp_5}, {pkp_4_score}, {pkp_5_score}
);""".format(
                data['id'], '2021-01-01 00:00:00.000000', **data, **score )

            print(raw_str)

            print('insert', ind, data['id'])

            test = session.execute(raw_str)

        session.commit()
        session.close()
        server.stop()
        return data['id']
    # except ValueError as error:
    #     print("Failed to insert record into mobile table", error)
    #     server.stop()
# insert_data_rfkm_no({'id':'sefsdsdf'))