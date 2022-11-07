CREATE PROCEDURE pa_SELECT_BENEFICIARIOS
AS
SELECT [id]
      ,[Nombre]
      ,[Apellidos]
      ,[Fecha_Nacimiento]
      ,[Curp]
      ,[Ssn]
      ,[Telefono]
      ,[Nacionalidad]
      ,[Porcentaje_Participacion]
      ,[Idempleados]
  FROM [dbo].[beneficiarios]
GO