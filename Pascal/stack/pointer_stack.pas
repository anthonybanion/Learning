{@brief implementasi stack dengan node linker
 @file pointer_stack.pas
 @date 06/01/2024
 @version 1.0}
program pointer_stack;
type
 fuit_name = string[20];
 node_linker = ^Tnodo;
  Tnodo = record
    data : fuit_name;
    next : node_linker;
  end;

procedure create_empty_stack(var top : node_linker);
begin
  top := nil;
end;

function is_empty(top : node_linker):boolean;
begin
  is_empty := top = nil;
end;

procedure insert_data(var top : node_linker; data : fuit_name);
var 
  new_node : node_linker;
begin
  new(new_node);
  new_node^.data := data;
  new_node^.next := top;
  top := new_node;
end;

procedure delete_data(var top : node_linker);
var 
  auxiliary : node_linker;
begin
  if not is_empty(top) then
  begin
    auxiliary := top;
    top := top^.next;
    dispose(auxiliary);
  end;
end;  

procedure print_data(top : node_linker);
begin
  if not is_empty(top) then
  begin
    writeln(top^.data);
    print_data(top^.next);
  end;
end;

var 
  top : node_linker;
begin
  create_empty_stack(top);
  insert_data(top, 'apple');
  insert_data(top, 'banana');
  insert_data(top, 'orange');
  print_data(top);
  delete_data(top);
  writeln;
  print_data(top);
   dispose(top^.next);
  Dispose(top);
 
  readln;
end.

    