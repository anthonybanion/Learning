program main;

{$mode objfpc}{$H+}

uses
  SysUtils,
  databaseConnection,   // connect to the database
  createTheUserTable,   // create the table using the already opened connection
  createUser;           // create a new user
begin
  ConnectToDB;
  CreateUsersTable;
  createUser.createUser;

  SQLiteConn.Close;

  WriteLn('👋 Program finished.');
end.
