CREATE OR REPLACE VIEW Preprocessing_tmp AS (
    SELECT 
      date_code
     ,CAST(pollen_scattering_num AS float) AS Pollen_scattering_num
    FROM
      pollen2
    GROUP BY
      date_char
)