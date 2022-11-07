CREATE PROCEDURE pa_UPDATE_EMPLEADOS
(
@Nombre VARCHAR(60)= 'N/A',
@Apellidos VARCHAR(60)= 'N/A',
@Fecha_Nacimiento AS DATE= '2022-10-02',
@Numero_Empleado AS INT= 1,
@Curp VARCHAR(60)= 'N/A',
@Ssn AS INT= 1,
@Telefono AS BIGINT= 1,
@Nacionalidad VARCHAR(60)= 'N/A',
@id AS INT
)
AS
BEGIN
UPDATE [dbo].[empleados]
	SET     Nombre = case when @Nombre = 'N/A' then Nombre else @Nombre end,
            Apellidos = case when @Apellidos = 'N/A' then Apellidos else @Apellidos end,
            Fecha_Nacimiento=case when @Fecha_Nacimiento= '2022-10-02' then Fecha_Nacimiento else @Fecha_Nacimiento end,
            Numero_Empleado=case when @Numero_Empleado= 1 then Numero_Empleado else @Numero_Empleado end,
            Curp=case when @Curp= 'N/A' then Curp else @Curp end,
            Ssn=case when @Ssn= 1 then Ssn else @Ssn end,
            Telefono=case when @Telefono= 1 then Telefono else @Telefono end,
            Nacionalidad=case when @Nacionalidad= 'N/A' then Nacionalidad else @Nacionalidad end
	WHERE id=@id 
END
