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
