program main;

{$mode objfpc}{$H+}

uses
  databaseConnection,   // connect to the database
  createTheUserTable,   // create the table using the already opened connection
  menu;
begin
  ConnectToDB;
  CreateUsersTable;
  menu.menu;

  SQLiteConn.Close;
end.