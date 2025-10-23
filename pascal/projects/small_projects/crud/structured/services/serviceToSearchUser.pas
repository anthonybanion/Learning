{*
  
  This unit provides a service to search for a user 
  in the database by their DNI (National ID).
  
  File: serviceToSearchUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToSearchUser;

{$mode objfpc}{$H+}

interface

function searchService(dni: String): Boolean;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection, global;

function searchService(dni: String): Boolean;
{*
  Searches for a user in the database by their DNI.
  
  @param dni The DNI of the user to search for.
  @return True if the user is found, False otherwise.
*}

var
  Query: TSQLQuery;
  begin
    Result := False;
    Query := TSQLQuery.Create(nil);
      try
        try
          Query.DataBase := SQLiteConn;
          Query.Transaction := SQLTransaction;

          Query.SQL.Text := 'SELECT * FROM users WHERE dni = :dni';
          Query.Params.ParamByName('dni').AsString := dni;

          Query.Open;

          if not Query.IsEmpty then
            begin
              // Assuming global variables are defined in a unit named 'global'
              global.id        := Query.FieldByName('id').AsInteger;
              global.firstName := Query.FieldByName('firstName').AsString;
              global.lastName  := Query.FieldByName('lastName').AsString;
              global.dni       := Query.FieldByName('dni').AsString;

              Result := True;
            end;
        except
          on E: Exception do
            WriteLn('Ocurrió un error: ', E.Message);
        end;
      finally
        Query.Free;
      end;
  end;
end.
