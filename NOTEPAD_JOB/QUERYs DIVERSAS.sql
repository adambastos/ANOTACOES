/*Trazer os registros onde o valor do campo email é NULL*/
SELECT NOME, SEXO, ENDERECO FROM CLIENTES WHERE EMAIL IS NULL;

/*Trazer os registros onde o valor do campo email não é NULL*/
SELECT NOME, SEXO, ENDERECO FROM CLIENTES WHERE EMAIL IS NOT NULL;

/*QUERY UPDATE*/
UPDATE FUNCIONARIOS SET EMAIL = 'CARLOS.SILVA@GMAIL.COM' WHERE EMAIL = 'CARLOS.SILVA@EMAIL.COM';

