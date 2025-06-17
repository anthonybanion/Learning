unit serviceToSearchUser;

{$mode objfpc}{$H+}

interface

function search(dni: String): Boolean;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection, global;

function search(dni: String): Boolean;
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
