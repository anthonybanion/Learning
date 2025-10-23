{*
  
  This unit provides a menu for a CRUD application 
  that allows users to create, update, read, 
  and delete user records.
  
  File: menu.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit menu;

{$mode objfpc}{$H+}

interface

procedure menu;

implementation

uses
  createUser, updateUser, readAllUsers, readUserByDni, deleteUser, global;

procedure menu;
{*
  Displays the main menu for the CRUD application.

  @return None
*}

var
    option : Integer;
begin
    option := 0;
    repeat
        WriteLn('*** Menu **');
        WriteLn('1. Create');
        WriteLn('2. Update user');
        WriteLn('3. Read user by DNI');
        WriteLn('4. Read all users');
        WriteLn('5. Delete user');
        WriteLn('6. Exit');
        WriteLn('');
        Writeln('Select an option (1-6): ');
        ReadLn(option);
        case option of
            1: begin
                    createUser.create;
                end;
            2: begin
                    updateUser.update;
                end;
            3: begin
                    readUserByDni.readByDni;
                end;
            4: begin
                    readAllUsers.readAll;
                end;
            5: begin
                    deleteUser.deleteUser;
                end;
            else
                WriteLn('Invalid option, please try again.');
        end;

    until (option = 6);

  WriteLn('👋 Program finished.');
end;
end.