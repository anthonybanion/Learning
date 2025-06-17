unit SearchUser;

{$mode objfpc}{$H+}

interface

function searchUser(dni : String): Boolean;

implementation

uses
    global, serviceToSearchUser;

function searchUser(dni : String): Boolean;
begin

  // Call the search function from the global unit
  if serviceToSearchUser.search(dni) then
    begin
        WriteLn('User found:');
        WriteLn('First Name: ', global.firstName);
        WriteLn('Last Name: ', global.lastName);
        WriteLn('DNI: ', global.dni);
        WriteLn(' ');
        Result := True;
    end
  else
    begin
        WriteLn('User not found.');
        Result := False;
    end;
end;
end.