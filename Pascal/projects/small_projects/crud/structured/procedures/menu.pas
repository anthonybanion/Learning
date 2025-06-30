unit menu;

{$mode objfpc}{$H+}

interface

procedure menu;

implementation

uses  
  createUser, updateUser, readAllUsers, readUserByDni, global;     

procedure menu;
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
                WriteLn('Exiting the program...');
                end;
            else
                WriteLn('Invalid option, please try again.');
        end;

    until (option = 5);

  WriteLn('👋 Program finished.');
end;
end.