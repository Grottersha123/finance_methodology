import logging

import psycopg2
from sqlalchemy import create_engine


def insert_data(data, score):
    try:
        from sshtunnel import SSHTunnelForwarder  # Run pip install sshtunnel
        from sqlalchemy.orm import sessionmaker  # Run pip install sqlalchemy

        with SSHTunnelForwarder(
                ('193.41.140.35', 22003),  # Remote server IP and SSH port
                ssh_username="analit",
                ssh_password="Sae7ZaeW",
                remote_bind_address=(
                'localhost', 5432)) as server:
            # PostgreSQL server IP and sever port on remote machine

            server.start()  # start ssh sever

            # connect to PostgreSQL
            local_port = str(server.local_bind_port)
            engine = create_engine('postgresql://iacmon:WCVaB90x5@127.0.0.1:' + local_port + '/data')
            # op2_3_score where op
            Session = sessionmaker(bind=engine)
            session = Session()
            # test data retrieval
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
            pfu14_score, pfu15_score, lp3_score, lp5_score,v3_score, pfu4, pfu5, pfu7, pfu8, pfu9)
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
            {},{},{},{},{});""".\
                format(data['id'],
                       data['op_1_d_t_delta'],data['op_2_d_t_max_percent_21'], data['op_3_d_t_max_delta_max_percent'],data['op_4_p_t_delta'],data['op_5'], data['op_6'], data['op_7'], data['op_8'],data['op_9'],
                                    data['pfu_3'], data['pfu_3a'], data['pfu_6'],
                                    # score['op_2_score']
                                    score['op_1_score'], score['op_5_score'],
                                    score['op_7_score'], score['op_8_score'], score['pfu_3_score'],
                                    score['pfu_6_score'], score['v_1_score'], score['v_2_score'],
                                    data['pfu_10_oc_1'], data['pfu_11'], data['pfu_12_oc_2'], data['pfu_13'],
                                    data['pfu_14'], data['pfu_15'], data['lp_3_ko_delta'], data['lp_5'],
                                    score['pfu_10_score'], score['pfu_12_score'], score['v_2_score'],
                                    score['pfu_14_score'], score['pfu_15_score'], score['lp_3_score'],
                                    score['lp_5_score'],score['v_3_score'],
                                    data['pfu_4'],data['pfu_5'],data['pfu_7'],data['pfu_8'],data['pfu_9']
                       )


            print(data['id'])
            test = session.execute(raw_str)
            session.commit()

            session.close()
            return data['id']
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        session.close()