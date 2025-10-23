{*
  
  Service to delete a user from the database by their DNI.
  
  File: serviceToDeleteUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToDeleteUser;

{$mode objfpc}{$H+}

interface

function deleteService(dni: String): Boolean;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function deleteService(dni: String): Boolean;
{*
  Deletes a user from the database by their DNI.

  @param dni The DNI of the user to delete.
  @return True if the user was deleted successfully, False otherwise.
*}

var
  Query: TSQLQuery;
begin
  Result := False;
  Query := TSQLQuery.Create(nil);
  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;

    Query.SQL.Text := 'DELETE FROM users WHERE dni = :dni';
    Query.ParamByName('dni').AsString := dni;

    Query.ExecSQL;
    SQLTransaction.Commit;
    Result := True;
  finally
    Query.Free;
  end;
end;

end.
