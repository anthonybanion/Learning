{*
  
  This unit provides a service to read user 
  details from the database by their DNI.
  
  File: serviceToReadUserByDni.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToReadUserByDni;

{$mode objfpc}{$H+}

interface

function readingServiceByDni(const Dni: String): String;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function readingServiceByDni(const Dni: String): String;
{*
  Reads user details from the database by their DNI.
  
  @param dni The DNI of the user to read.
  @return A string with the user details or a "not found" message.
*}

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
