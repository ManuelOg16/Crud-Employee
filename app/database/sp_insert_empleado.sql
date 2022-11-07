CREATE PROCEDURE pa_INSERT_EMPELADOS
(
@Nombre VARCHAR(60),
@Apellidos VARCHAR(60),
@Fecha_Nacimiento AS DATE,
@Numero_Empleado AS INT,
@Curp VARCHAR(60),
@Ssn AS INT,
@Telefono AS BIGINT,
@Nacionalidad VARCHAR(60)
)
AS
BEGIN
INSERT INTO [dbo].[empleados]
    (Nombre
    ,Apellidos
    ,Fecha_Nacimiento
    ,Numero_Empleado
    ,Curp
    ,Ssn
    ,Telefono
    ,Nacionalidad)
VALUES(@Nombre,@Apellidos,@Fecha_Nacimiento,@Numero_Empleado,@Curp,@Ssn,@Telefono,@Nacionalidad)
SELECT @@IDENTITY AS Id
END

