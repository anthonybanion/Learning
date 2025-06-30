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
{ 
  This function reads all users from the database.
  It returns a list of strings with user details.
}
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
