{*
  
  This unit establishes a connection to an SQLite database
  
  File: databaseConnection.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit databaseConnection;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, sqlite3conn, sqldb, global;

var
  SQLiteConn: TSQLite3Connection;
  SQLTransaction: TSQLTransaction;

procedure ConnectToDB;

implementation

procedure ConnectToDB;
{*
  Connects to the SQLite database using the specified path.

  @param dbPath The path to the SQLite database file.
  @return None
*}

begin

  global.dbPath := './database/users.db'; // Set the database path

// The connection is started
  SQLiteConn := TSQLite3Connection.Create(nil);
  SQLTransaction := TSQLTransaction.Create(nil);

  try
    // Path to the SQLite database file
    SQLiteConn.DatabaseName :=  global.dbPath;

    // Associate the transaction
    SQLiteConn.Transaction := SQLTransaction;

    // Open the connection
    SQLiteConn.Open;

    // Start the transaction
    SQLTransaction.StartTransaction;

    WriteLn('✅ Connection to database established successfully.');

  except
    on E: Exception do
      WriteLn('❌ Error connecting to database: ', E.Message);
  end;
end;

end.
