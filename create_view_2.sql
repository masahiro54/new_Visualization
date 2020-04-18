CREATE OR REPLACE VIEW Preprocessing AS (
    SELECT 
      date_code 
     ,Pollen_scattering_num
   --5項移動平均
     ,AVG(Pollen_scattering_num)OVER(ORDER BY date_code ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS col5_avg
    FROM
      Preprocessing_tmp

)