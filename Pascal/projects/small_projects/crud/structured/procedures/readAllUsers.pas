unit readAllUsers;

{$mode objfpc}{$H+}

interface
Procedure readAll();

implementation

uses
  Classes, serviceToReadToAllUser;

Procedure readAll();

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
