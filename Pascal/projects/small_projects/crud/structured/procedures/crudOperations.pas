program crudOperations;

{$mode objfpc}{$H+}

uses
  SysUtils, db_connection;

begin
  ConnectToDB;

  // Aquí va el resto del CRUD
  // Por ejemplo: CreateUser(); ListUsers(); etc.

  // ¡No olvides cerrar la conexión al terminar!
  SQLTransaction.Commit;
  SQLiteConn.Close;
end.
