COPY(
SELECT XMLELEMENT(NAME WAREHOUSES, XMLAGG(WAREHOUSE)) FROM
(select 
 XMLELEMENT(NAME WAREHOUSE,
   XMLELEMENT(NAME ID, w.w_id),
   XMLELEMENT(NAME NAME, w.w_name),
   XMLELEMENT(NAME STREET, w.w_street),
   XMLELEMENT(NAME CITY, w.w_city),
   XMLELEMENT(NAME COUNTRY, w.w_country),
   XMLELEMENT(NAME ITEMS, 
   XMLAGG(
   XMLELEMENT(NAME ITEM,
		XMLELEMENT(NAME i_id,i.i_id),
		XMLELEMENT(NAME im_id, i.i_im_id ),
		XMLELEMENT(NAME NAME, i.i_name),
		XMLELEMENT(NAME PRICE, i.i_price),
		XMLELEMENT(NAME QTY, s.s_qty)) order by i.i_id))) WAREHOUSE
from
warehouse w inner join 
stock s on w.w_id = s.w_id inner join
item i on s.i_id = i.i_id
group by w.w_id
order by w.w_id)a) to 'D:\Userdata\Desktop\q1.xml'