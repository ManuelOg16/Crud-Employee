CREATE PROCEDURE pa_SELECT_EMPLEADO_X_ID_SUMA
(
@Idempleados AS INT
)
AS
BEGIN
SELECT DISTINCT Idempleados ,sum(Porcentaje_Participacion)
    FROM [dbo].[beneficiarios]
    WHERE Idempleados=@Idempleados
    GROUP BY Idempleados
END
