CREATE PROCEDURE pa_SELECT_EMPLEADO_X_ID
(
@id AS INT
)
AS
BEGIN
SELECT [id]
  FROM [dbo].[empleados]
  WHERE id=@id 
END