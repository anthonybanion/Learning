{*
  
  Searches for a user by their DNI in the database 
  and displays their details if found.
  
  File: searchUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit searchUser;

{$mode objfpc}{$H+}

interface

function search(dni : String): Boolean;

implementation

uses
    global, serviceToSearchUser;

function search(dni : String): Boolean;
{*
  Searches for a user in the database by their DNI.

  @param dni The DNI of the user to search for.
  @return True if the user is found, False otherwise.
*}

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