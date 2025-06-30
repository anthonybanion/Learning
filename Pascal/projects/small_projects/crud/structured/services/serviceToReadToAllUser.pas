{*
  
  This unit provides a service to read all users 
  from the database.
  
  File: serviceToReadToAllUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit serviceToReadToAllUser;

{$mode objfpc}{$H+}

interface
uses
Classes;

function readingServiceToAllUser(): TStringList;

implementation

uses
    SysUtils, sqlite3conn, sqldb, db, databaseConnection;

function readingServiceToAllUser(): TStringList;
{*
  Reads all users from the database and returns a 
  
  list of user details.
  @return A TStringList containing user details.
*}

var
  Query: TSQLQuery;
  UserList: TStringList;
  i: Integer;
begin
  UserList := TStringList.Create;
  Query := TSQLQuery.Create(nil);
  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;
    Query.SQL.Text := 'SELECT firstName, lastName, dni FROM users';
    Query.Open;
    i := 0;
    while not Query.EOF do
    begin
      UserList.Add(Format('User %d: %s, %s, %s', [
        i + 1,
        Query.FieldByName('firstName').AsString,
        Query.FieldByName('lastName').AsString,
        Query.FieldByName('dni').AsString
      ]));
      Query.Next;
      Inc(i);
    end;

    if UserList.Count = 0 then
    begin
      UserList.Add('No users found.');
    end;
  finally
    Query.Free;
  end;
  Result := UserList;
end;

end.
