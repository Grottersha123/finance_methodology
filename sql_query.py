raw_sql = [
           """
           select * from fk_form_0503769_r1_20210226
      where period='01012020' and blocksubbo_codesub='07505001X435400000001' and accountcode in ('30211','30301','30402','30403') and kbk='*****************'
           """,

           """
           select kvd from fk_form_0503779 group by kvd
         """,

           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r1 
           where 
               strcode='010' 
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- d_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354|001X6063)%'
           group by period, blocksubbo_codesub
              """,
           """
                select 
                    substring(blocksubbo_codesub from 6 for 8) as id,
                    period, 
                    blockactionkind_id as form,
                    sum(total) as d
                from fk_form_0503737_r1 
                where 
                    strcode='010' 
                    and blockactionkind_id in (2,4,5,7)
                    and blocktypereport_id<>1
                    and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
                    and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
                group by blockactionkind_id, period, blocksubbo_codesub
                order by period, blockactionkind_id, blocksubbo_codesub
                     """,

           """
 select
     substring(blocksubbo_codesub from 6 for 8) as id,
     period,
     sum(total) as d
 from fk_form_0503737_r1 
 where 
     strcode='010' 
     and blockactionkind_id in (2,4,5,7)
     and blocktypereport_id<>1
     and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
     and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
 group by period, blocksubbo_codesub
 """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               strcode='200' 
               and blockactionkind_id in (2,4,7)
               and codeanalytic='***' 
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           
           """,

           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               blockactionkind_id in (2,4,7)
               and blockmrkpfhd_code='111' 
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           
           """,
           """
 select 
     substring(blocksubbo_codesub from 6 for 8) as id,
     period,
     sum(yearbalance) as d
 from fk_form_0503779 
 where 

     kvd in ('2','4','7') 
     and blockformsections_id in (34,35,36) 
     and blocktypereport_id<>1
     and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
     and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
 group by period, blocksubbo_codesub
 
 """,
           """
           
 select 
     substring(blocksubbo_codesub from 6 for 8) as id,
     period,
     sum(yearbalance) as d
 from fk_form_0503779 
 where 
     kvd in ('2') 
     and blockformsections_id in (34,35,36) 
     and blocktypereport_id<>1
     and period in ('01012021', '01012020')
     and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
 group by period, blocksubbo_codesub
 """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               strcode='200' 
               and blockactionkind_id in (2)
               and codeanalytic='***' 
               and blocktypereport_id<>1

               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           
           """,
           """

           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r3 
           where 
               --static filters
               strcode='520' 
               and blockmrkpfhd_code='710'
               and blockactionkind_id in (2) 
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           
           """,
           """
           --z_t_um
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r3 
           where 
               --static filters
               strcode='520' 
               and blockmrkpfhd_code='810'
               and blockactionkind_id in (2) 
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """
    ,
           """
           --d_t_o
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(abringinck) as d
           from fk_form_0503730_r1 
           where 
               --static filters
               strcode='400'
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               blockactionkind_id as form,
               sum(appz) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (2)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by blockactionkind_id, period, blocksubbo_codesub
           order by period, blockactionkind_id, blocksubbo_codesub
           """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               blockactionkind_id as form,
               sum(appz) as d
           from fk_form_0503737_r3 
           where 
               strcode='520' 
               and blockmrkpfhd_code='710'  
               and blockactionkind_id in (2)
               and blocktypereport_id<>1
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by blockactionkind_id, period, blocksubbo_codesub
           order by period, blockactionkind_id, blocksubbo_codesub
           """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               blockactionkind_id as form,
               sum(appz) as d
           from fk_form_0503737_r3 
           where 
               strcode='520' 
               and blockmrkpfhd_code='810'  
               and blockactionkind_id in (2)
               and blocktypereport_id<>1
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by blockactionkind_id, period, blocksubbo_codesub
           order by period, blockactionkind_id, blocksubbo_codesub
           """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(abringinck) as d
           from fk_form_0503730_r1 
           where 
               strcode in ('250','260','270','280')
               and blocktypereport_id<>1
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(abringinck) as d
           from fk_form_0503730_r1 
           where 
               strcode in ('400','410','420','430','470')
               and blocktypereport_id<>1
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """,
           """
           --kz_pros
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(overduedebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               blockactionkind_id in (2,4,7)
               and accountcode='*****'
               and blocktypedebt_id=2
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """,
           """
           --dz_pros
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(overduedebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               blockactionkind_id in (2,4,7)
               and accountcode='*****'
               and blocktypedebt_id=1
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """,
           """
           --vb_t
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(totalk) as d
           from fk_form_0503730_r1 
           where 
               --static filters
               strcode='350'
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """,
           """
           --os
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(endbalance) as d
           from fk_form_0503779 
           where 
               --static filters
               kvd in ('2','4','7') 
               and blockformsections_id in (34,35,36) 
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --kz_zpvf
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(totaldebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               kvd in ('2','4','7') 
               and accountcode in ('21100','21300','30100','30200','30600','30700','30800','30900','31000','31100','40200','40300')
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --kz_pr - ���������� ���������� ��������� ���
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(totaldebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               kvd in ('2','4','7') 
               and accountcode  not in ('*****','50000','21100','30100','40200','40300','21300','30200','30600','30700','30800','30900','31000','31100')
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --fot_p
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(appz) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               blockactionkind_id in ('2','4','7') 
               and blockmrkpfhd_code in ('111')
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(totaldebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               kvd in ('2','4','7') 
               and accountcode in ('30211','30301','30402','30403')
               and kbk='*****************'
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --kz_vf
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(totaldebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               kvd in ('2','4','7') 
               and accountcode in ('30213','30302','30306','30307','30308','30309','30310','30311')
               and kbk='*****************'
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --p_f
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(appz) as d
           from fk_form_0503737_r2 
           where 
               blockactionkind_id in ('2','4','7') 
               and blockmrkpfhd_id in (117)
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               blockactionkind_id in ('2','4','7') 
               and blockmrkpfhd_id in (117)
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               blockactionkind_id in ('2','4','7') 
               and blockmrkpfhd_code in ('111')
               and blocktypereport_id<>1
               and period in ('01012021', '01012020') -- p_t_m_1 - ���� �� ������, �� �� 1 ��� ������, �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --kz_zpng - ��� �� ����������, ��� � kz_zp, �� � ������ �������� �����. ������ ��� ���������� � �������
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(totaldebtk) as d
           from fk_form_0503769_r1 
           where 
               --static filters
               kvd in ('2','4','7') 
               and accountcode in ('30211','30301','30402','30403')
               and kbk='*****************'
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --z_1_pdd
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r3 
           where 
               --static filters
               blockactionkind_id in ('2') 
               and strcode='520' 
               and blockmrkpfhd_id=189 
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --z_2_pdd
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period,
               sum(total) as d
           from fk_form_0503737_r3 
           where 
               --static filters
               blockactionkind_id in ('2') 
               and strcode='520' 
               and blockmrkpfhd_id=192 
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --d_pt_pdd + d_tp_pdd + pd_1_d_t_pdd - ����� ����� ���������� 3 �������� �������, ���� �������� ������� 1
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (2)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --d_tf_oms - ����� ����� ���������� 3 ����
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(total) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --pd_1_d_t_oms
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --pd_2_d_t_gz
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (4)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --Fot_tf - ����� ����� 3 ���� ����������
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               blockmrkpfhd_id=123 
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --Fot_tp
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               blockmrkpfhd_id=123 
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --VF_tf - ����� ����� 3 ���� ����������
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               blockmrkpfhd_id=126 
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --VF_tp
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               blockmrkpfhd_id=126 
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --P_tf - ����� ����� 3 ���� ����������
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(total) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               strcode='200' 
               and codeanalytic not in ('***','111','119')
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --P_tp
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r2 
           where 
               --static filters
               strcode='200' 
               and codeanalytic not in ('***','111','119')
               and blockactionkind_id in (2,4,7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --D_tf
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(appz) as d
           from fk_form_0503737_r1 
           where 
               --static filters
               strcode='010' 
               and blockactionkind_id in (7)
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020') 
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           """,
           """
           --vla_t
           select 
               substring(blocksubbo_codesub from 6 for 8) as id,
               period, 
               sum(abringinck) as d
           from fk_form_0503730_r1 
           where 
               --static filters
               strcode in ('200','240')
               and blocktypereport_id<>1
               --variable filters
               and period in ('01012021', '01012020')  -- ����� ����� �������� �� 2 �������� �������: ������� � ������� (�� 1 ��� ������), �.�. � �������: 01012020
               and blocksubbo_codesub SIMILAR TO '%(001X4354)%'
           group by period, blocksubbo_codesub
           order by period, blocksubbo_codesub
           """]
