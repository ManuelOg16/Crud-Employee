CREATE PROCEDURE pa_DELETE_EMPLEADO
(
@id AS INT
)
AS
BEGIN
DELETE FROM [dbo].[empleados] WHERE id=@id 
END