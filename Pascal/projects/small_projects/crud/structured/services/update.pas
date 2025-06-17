unit update;

{$mode objfpc}{$H+}

interface
procedure updateUser;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

procedure updateUser;
var
  Query: TSQLQuery;
  firstName, lastName, dni: string;
  userId: Integer;
begin
    // Create the database connection
    Query := TSQLQuery.Create(nil);

    try
        Query.DataBase := SQLiteConn;
        Query.Transaction := SQLTransaction;

        Query.ExecSQL;
        SQLTransaction.Commit;
        WriteLn('User update successfully.');
    finally
        Query.Free;
    end;
end;
end.