program main;

{$mode objfpc}{$H+}

uses
  SysUtils,
  databaseConnection,   // connect to the database
  createTheUserTable;   // create the table using the already opened connection

begin
  ConnectToDB;
  CreateUsersTable;
  SQLiteConn.Close;

  WriteLn('👋 Program finished.');
end.
