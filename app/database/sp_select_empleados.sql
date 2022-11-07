CREATE PROCEDURE pa_SELECT_EMPLEADOS
AS
SELECT [id]
      ,[Nombre]
      ,[Apellidos]
      ,[Fecha_Nacimiento]
      ,[Numero_Empleado]
      ,[Curp]
      ,[Ssn]
      ,[Telefono]
      ,[Nacionalidad]
  FROM [dbo].[empleados]
GO