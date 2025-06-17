unit updateUser;

{$mode objfpc}{$H+}

interface
procedure updateUser;

implementation

uses
  serviceToUpdateUser, searchUser, global;

procedure updateUser;
{ This procedure updates an existing user in the database.
  It returns a message indicating the success or failure of the operation. }
var 
   dni: String;
   firstName, lastName: String;
begin
    Write('Enter DNI: ');
    ReadLn(dni);
    if searchUser.searchUser(dni) then
      begin
          WriteLn('User found:');
          WriteLn('Enter new first name (or press Enter to keep current): ');
          ReadLn(firstName);
          WriteLn('Enter new last name (or press Enter to keep current): ');
          ReadLn(lastName);
          
          if (firstName <> '') or (lastName <> '') then
            begin
                serviceToUpdateUser.update(global.id, firstName, lastName);
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