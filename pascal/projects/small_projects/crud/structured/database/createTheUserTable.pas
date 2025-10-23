{*
  
  This unit contains the procedure to create the 
  "users" table in the SQLite database.
  
  File: createTheUserTable.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit createTheUserTable;

{$mode objfpc}{$H+}

interface

procedure CreateUsersTable;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db,
  databaseConnection; // We import the unit where SQLiteConn and SQLTransaction are

procedure CreateUsersTable;
{*
  Creates the "users" table in the SQLite database 
  if it does not exist.

  @param None
  @return None
*}

var
  Query: TSQLQuery;
begin
  Query := TSQLQuery.Create(nil);
  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;

    Query.SQL.Text :=
      'CREATE TABLE IF NOT EXISTS users (' +
      'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
      'firstName TEXT NOT NULL, ' +
      'lastName TEXT NOT NULL, ' +
      'dni TEXT UNIQUE NOT NULL);';

    Query.ExecSQL;

    // Confirmamos la transacción
    SQLTransaction.Commit;

    WriteLn('✅ Table "users" created successfully.');

  except
      on E: Exception do
        WriteLn('❌ Error creating table: ', E.Message);
  end;
  

  Query.Free;
end;

end.
