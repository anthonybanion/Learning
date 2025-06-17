unit menu;

{$mode objfpc}{$H+}

interface

procedure menu;

implementation

uses  
  createUser, updateUser;     

procedure menu;
var
    option : Integer;
begin
    option := 0;
    repeat
        WriteLn('*** Menu **');
        WriteLn('1. Create');
        WriteLn('2. Update user');
        WriteLn('3. Delete user');
        WriteLn('4. List users');
        WriteLn('5. Exit');
        WriteLn('');
        Writeln('Select an option (1-5): ');
        ReadLn(option);
        case option of
            1: begin
                    createUser.createUser;
                end;
            2: begin
                    updateUser.updateUser;
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