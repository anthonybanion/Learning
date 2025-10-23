{*
  
  This unit provides a service to create a new user 
  in the database.
  
  File: serviceToCreateUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToCreateUser;

{$mode objfpc}{$H+}

interface 

function creationService(firstName, lastName, dni: string): String;

implementation

uses
  Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function creationService(firstName, lastName, dni: string): String;
{*
  Creates a new user in the database with the provided details.

  @param firstName The first name of the user.
  @param lastName The last name of the user.
  @param dni The DNI of the user.
  @return A message indicating the success or failure of the operation.
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
