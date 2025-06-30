unit searchUser;

{$mode objfpc}{$H+}

interface

function search(dni : String): Boolean;

implementation

uses
    global, serviceToSearchUser;

function search(dni : String): Boolean;
begin

  // Call the search function from the global unit
  if serviceToSearchUser.searchService(dni) then
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