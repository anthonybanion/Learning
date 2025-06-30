unit serviceToUpdateUser;

{$mode objfpc}{$H+}

interface

procedure updateService(id: Integer; firstName, lastName : string);

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

procedure updateService(id: Integer; firstName, lastName : string);
{ This procedure updates an existing user in the database.
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
    Query.SQL.Text := 'UPDATE users SET firstName = :firstName, lastName = :lastName WHERE id = :id';
    Query.Params.ParamByName('id').AsInteger := id;
    Query.Params.ParamByName('firstName').AsString := firstName;
    Query.Params.ParamByName('lastName').AsString := lastName;
    Query.ExecSQL;
    SQLTransaction.Commit;

  finally
    Query.Free;
  end;
end;
end.
