{*
  
  This program is a simple CRUD application in Pascal 
  that connects to an SQLite database.
  
  File: main.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


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