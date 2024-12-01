{@brief This program is a simple example of a linked_list.
 @details This program creates a linked_list of 5 nodes and prints the_list.
 @date 04/01/2024
 @version 1.0}
Program linked_list;
type
 node_linker = ^node;
  node = record
    data : integer;
    next : node_linker;
  end;
  
procedure initialize_list(var head, tail : node_linker);
begin
    new(head);
    head^.data := 0;
    tail := head;
end;

procedure add_node(var head, tail : node_linker; data : integer);
var
    auxiliary : node_linker;
begin 
    new(auxiliary);
    auxiliary^.data := data;
    tail^.next := auxiliary;
    tail := auxiliary;
    tail^.next := nil;
end;

procedure print_list(head : node_linker);
begin
    while head <> nil do
    begin
        writeln(head^.data);
        head := head^.next;
    end;

end;

var
    head, tail : node_linker;
    i : integer;
begin
    clrscr;
    initialize_list(head, tail);
    
    for i:= 1 to 5 do
    add_node(head, tail, i);
    
    print_list(head);
    readln;
end.