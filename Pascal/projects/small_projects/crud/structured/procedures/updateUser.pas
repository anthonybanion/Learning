{*
  
  This unit provides a procedure to update an 
  existing user in the database.
  
  File: updateUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit updateUser;

{$mode objfpc}{$H+}

interface
procedure update;

implementation

uses
  serviceToUpdateUser, searchUser, global;

procedure update;
{*
  Updates an existing user in the database.

  @param id The ID of the user to update.
  @param firstName The new first name of the user.
  @param lastName The new last name of the user.
*}

var 
   dni: String;
   firstName, lastName: String;
begin
    Write('Enter DNI: ');
    ReadLn(dni);
    if searchUser.search(dni) then
      begin
          WriteLn('User found:');
          WriteLn('Enter new first name (or press Enter to keep current): ');
          ReadLn(firstName);
          WriteLn('Enter new last name (or press Enter to keep current): ');
          ReadLn(lastName);
          
          if (firstName <> '') or (lastName <> '') then
            begin
                serviceToUpdateUser.updateService(global.id, firstName, lastName);
                WriteLn('User updated successfully.');
            end
          else
            begin
                WriteLn('No changes made to the user.');
            end;
      end
    else
      begin
          WriteLn('User not updated.');
      end;
    global.id := 0;
    global.firstName := '';
    global.lastName := '';
    global.dni := '';
end;
end.