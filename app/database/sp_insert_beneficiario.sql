CREATE PROCEDURE pa_INSERT_BENEFICIARIOS
(
@Nombre VARCHAR(60),
@Apellidos VARCHAR(60),
@Fecha_Nacimiento AS DATE,
@Curp VARCHAR(60),
@Ssn AS INT,
@Telefono AS BIGINT,
@Nacionalidad VARCHAR(60),
@Porcentaje_Participacion AS INT,
@Idempleados AS INT
)
AS
BEGIN
INSERT INTO [dbo].[beneficiarios]
    (Nombre
    ,Apellidos
    ,Fecha_Nacimiento
    ,Curp
    ,Ssn
    ,Telefono
    ,Nacionalidad
    ,Porcentaje_Participacion
    ,Idempleados)
VALUES(@Nombre,@Apellidos,@Fecha_Nacimiento,@Curp,@Ssn,@Telefono,@Nacionalidad,@Porcentaje_Participacion,@Idempleados)
SELECT @@IDENTITY AS Id
END

