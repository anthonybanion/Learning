{*
  
  This unit provides a procedure to read all users 
  from the database and display their details.
  
  File: readAllUsers.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit readAllUsers;

{$mode objfpc}{$H+}

interface
Procedure readAll();

implementation

uses
  Classes, serviceToReadToAllUser;

Procedure readAll();
{*
  Reads all users from the database and displays their details.

  @return A TStringList containing user details.
*}

var
  UserList: TStringList;
  i: Integer;
begin
  UserList := serviceToReadToAllUser.readingServiceToAllUser();
  try
    for i := 0 to UserList.Count - 1 do
    begin
      WriteLn(UserList[i]);
    end;
  finally
    UserList.Free;
  end;
end;

end.
