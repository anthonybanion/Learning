{@brief Implementasi stack dengan record
 @file record_stack.pas
 @date 06/01/2024
 @version 1.0}

program record_stack;
const 
    max=50;
type
    number_element = integer;
    Tstack = record
         top  : 0 ..max;
        stack_data :array[1..max] of number_element;
    end;
var
    stack: Tstack;
    i:integer;

procedure create_empty_stack(var stack:Tstack);
begin
    stack.top:=0;
end;

function is_empty(stack:Tstack):boolean;
begin
    is_empty:=stack.top=0;
end;

function is_full(stack:Tstack):boolean;
begin
    is_full:=stack.top=max;
end;

procedure insert_data(var stack:Tstack; element:number_element);
begin
    if not is_full(stack) then
    begin
        stack.top:=stack.top+1;
        stack.stack_data[stack.top]:=element;
    end;
end;

procedure print_data(stack:Tstack);
var
    i:integer;
begin    
    for i:=stack.top downto 1 do
    begin
        writeln(stack.stack_data[i]);
    end;
end;

function delete_data(var stack:Tstack):number_element;
begin
    if not is_empty(stack) then
    begin
        delete_data:=stack.stack_data[stack.top];
        stack.top:=stack.top-1;
    end;
end;
function top(stack:Tstack):number_element;
begin
    if not is_empty(stack) then
    begin
        top:=stack.stack_data[stack.top];
    end;
end;
begin
    create_empty_stack(stack);
    for i:=1 to 10 do
    begin
        insert_data(stack,i);
    end;
    print_data(stack);
    writeln('top : ',top(stack));
    writeln('delete_data :',delete_data(stack));
    writeln('top : ',top(stack));
    readln;
end.
    