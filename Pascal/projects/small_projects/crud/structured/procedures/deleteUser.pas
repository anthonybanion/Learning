{*
  
  This unit provides a procedure to delete a user 
  from the database.
  
  File: deleteUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit deleteUser;

{$mode objfpc}{$H+}
interface
procedure deleteUser();
implementation

uses
  serviceToDeleteUser, global;

procedure deleteUser();
{*
    Deletes a user from the database by their DNI.

  @param dni The DNI of the user to delete.
  @return True if the user was deleted successfully, False otherwise.
*}

var 
    dni: String;
begin
  Write('Enter DNI of the user to delete: ');
  ReadLn(dni);
  if serviceToDeleteUser.deleteService(dni) then
    WriteLn('User deleted successfully.')
  else
    WriteLn('User not found or could not be deleted.');

end;

end.