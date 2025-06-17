unit serviceToCreateUser;

{$mode objfpc}{$H+}

interface 

function create(firstName, lastName, dni: string): String;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function create(firstName, lastName, dni: string): String;
{ This function creates a new user in the database.
  It returns a message indicating the success or failure of the operation. }
var
  Query: TSQLQuery;

begin
  // Create the database connection
  Query := TSQLQuery.Create(nil);

  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;

    // Prepare and execute the SQL query
    Query.SQL.Text := 'INSERT INTO users (firstName, lastName, dni) VALUES (:firstName, :lastName, :dni)';
    Query.ParamByName('firstName').AsString := firstName;
    Query.ParamByName('lastName').AsString := lastName;
    Query.ParamByName('dni').AsString := dni;
    Query.ExecSQL;
    SQLTransaction.Commit;
    Result := 'User created successfully.';

  finally
    Query.Free;
  end;
end;
end.
