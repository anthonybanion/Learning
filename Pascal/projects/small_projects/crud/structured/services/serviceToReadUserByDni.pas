unit serviceToReadUserByDni;

{$mode objfpc}{$H+}

interface

function readingServiceByDni(const Dni: String): String;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function readingServiceByDni(const Dni: String): String;
{ 
  This function reads a user from the database using their DNI.
  It returns a string with user details if found, or a "not found" message.
}
var
  Query: TSQLQuery;
begin
  Result := ''; // Default result
  Query := TSQLQuery.Create(nil);
  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;
    Query.SQL.Text := 'SELECT firstName, lastName, dni FROM users WHERE dni = :dni';
    Query.Params.ParamByName('dni').AsString := Dni;
    Query.Open;

    if not Query.IsEmpty then
    begin
      Result := Format('User found: %s, %s, %s', [
        Query.FieldByName('firstName').AsString,
        Query.FieldByName('lastName').AsString,
        Query.FieldByName('dni').AsString
      ]);
    end
    else
    begin
      Result := 'User not found.';
    end;
  finally
    Query.Free;
  end;
end;

end.
