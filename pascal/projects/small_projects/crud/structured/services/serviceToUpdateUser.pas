{*
  
  This unit provides a procedure to update an existing 
  user in the database.
  
  File: serviceToUpdateUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToUpdateUser;

{$mode objfpc}{$H+}

interface

procedure updateService(id: Integer; firstName, lastName : string);

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

procedure updateService(id: Integer; firstName, lastName : string);
{*
  Updates an existing user in the database.
  
  @param id The ID of the user to update.
  @param firstName The new first name of the user.
  @param lastName The new last name of the user.
*}

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
